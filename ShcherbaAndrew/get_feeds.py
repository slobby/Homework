# -*- coding: utf-8 -*-
"""date_type module."""

from typing import List, Union
from bs4.element import NavigableString, Tag
from utils import date_type
from errors import GetFeedException
from app_logger import get_logger
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from errors import (
    EmptyHTTPResponseException,
    WrongXMLContetException,
    EmptyXMLTagException,
)
from interfaces import ProgramArgs, ImageClass, EntryClass, FeedClass
from constants import TIMEOUT, TAG_RE

logger = get_logger(__name__)


def get_feeds(params: ProgramArgs) -> List[FeedClass]:
    """Get feeds.

    Args:
        params (ProgramArgs): command line params

    Returns:
        List[FeedClass]: List of FeedClass entities
    """
    feeds = []
    if params.date is None:
        feeds.append(get_feed_from_URL(params))
    else:
        feeds.extend(get_feed_from_storage(params))
    return feeds


def get_feed_from_URL(params: ProgramArgs) -> Union[FeedClass, None]:
    """Get feed from URL.

    Args:
        params (ProgramArgs): command line params

    Raises:
        EmptyHTTPResponseException: Raise when response = None
        GetFeedException: Raised when there was a error while fetching data from URL, for above located code

    Returns:
        Union[FeedClass, None]:  FeedClass entity
    """
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = None
    try:
        response = requests.get(url=params.source, timeout=TIMEOUT, verify=False)
        if response is None:
            raise EmptyHTTPResponseException()
    except EmptyHTTPResponseException:
        logger.error(f"Get empty response from source [{params.source}]")
    except requests.RequestException as ex:
        logger.error(
            f"There was an exception that occurred while handling [{params.source}]. Exception - {ex}"
        )
    except Exception as ex:
        print(ex)
    else:
        return parse_to_feed(response)
    raise GetFeedException(sourse=params.source)


def get_feed_from_storage(params: ProgramArgs):
    """Unrealised.

    Args:
        params (ProgramArgs): [description]
    """
    pass


def parse_to_feed(req: requests.Response) -> Union[FeedClass, None]:
    """Parse xml to FeedClass entity.

    Args:
        req (requests.Response): response from URL

    Raises:
        EmptyXMLTagException: Raised when couldn`t found tag <channel> in response.content
        WrongXMLContetException: Raised when couldn`t found tag <channel> in response.content for above located code

    Returns:
        Union[FeedClass, None]: FeedClass entity
    """
    feed = None
    try:
        soup = BeautifulSoup(req.content, features="xml")
        channel_tag = soup.channel
        if channel_tag is None:
            raise EmptyXMLTagException()
        title = extract_string_from_tag(channel_tag, "title", req.url)
        link = extract_string_from_tag(channel_tag, "link", req.url)
        description = extract_string_from_tag(channel_tag, "description", req.url)
        published = extract_string_from_tag(channel_tag, "pubDate", req.url)
        published_parsed = None
        if published:
            published_parsed = date_type(
                published,
                "%a, %d %b %Y %H:%M:%S %z",
            )
        image = parse_to_image(channel_tag.image, req.url)
        entries = parse_items(channel_tag.find_all("item"), req.url)
        feed = FeedClass(
            title=title,
            link=link,
            image=image,
            description=description,
            published=published,
            published_parsed=published_parsed,
            entries=entries,
        )
    except EmptyXMLTagException:
        logger.error(f"Couldn`t found <chanel> tag in xml, from source [{req.url}]")
    else:
        return feed
    raise WrongXMLContetException(sourse=req.url)


def parse_to_image(
    image_tag: Union[Tag, None], req_url: str
) -> Union[ImageClass, None]:
    """Parse rss tag <image> to ImageClass entity.

    Args:
        image_tag (Union[Tag, None]): suggested tag <image>
        req_url (str): xml url

    Returns:
        ImageClass: ImageClass entity
    """
    image = None
    if image_tag is not None:
        title = extract_string_from_tag(image_tag, "title", req_url)
        url = extract_string_from_tag(image_tag, "url", req_url)
        link = extract_string_from_tag(image_tag, "link", req_url)
        width = extract_string_from_tag(image_tag, "width", req_url)
        height = extract_string_from_tag(image_tag, "height", req_url)
        description = extract_string_from_tag(image_tag, "description", req_url)
        image = ImageClass(
            title=title,
            url=url,
            link=link,
            width=width,
            height=height,
            description=description,
        )
    return image


def parse_items(
    items_tag_list: Union[List[Tag], None], req_url: str
) -> List[EntryClass]:
    """Parse rss tag <items> to EntryClass entities.

    Args:
        items_tag_list (Union[List[Tag], None]): list of suggested tag <item>
        req_url (str): xml url

    Returns:
        List[EntryClass]: exctracted List of EntryClass entities, or None if couldn`t exctracted, or items_tag_list is None
    """
    entries = []
    if items_tag_list:
        for item in items_tag_list:
            title = extract_string_from_tag(item, "title", req_url)
            link = extract_string_from_tag(item, "link", req_url)
            description = extract_string_from_tag(item, "description", req_url)
            description_parsed = None
            if description:
                description_parsed = remove_tags(description)
            published = extract_string_from_tag(item, "pubDate", req_url)
            published_parsed = None
            if published:
                published_parsed = date_type(
                    published,
                    "%a, %d %b %Y %H:%M:%S %z",
                )
            guid = extract_string_from_tag(item, "guid", req_url)
            entry = EntryClass(
                title=title,
                link=link,
                description=description,
                description_parsed=description_parsed,
                published=published,
                published_parsed=published_parsed,
                guid=guid,
            )
            entries.append(entry)
    return entries


def extract_string_from_tag(parent_tag: Tag, name: str, url: str) -> Union[str, None]:
    """Exctract NavigableString from Tag, and convert to unicode.

    Args:
        parent_tag (Tag): parent tag
        name (str): suggested tag name
        url (str): xml url

    Returns:
        Union[str, None]: exctracted string, or None if couldn`t exctracted, or target_tag is None
    """
    string = None
    # target_tags = parent_tag.find_all(name)
    for inner_tag in parent_tag.children:
        if isinstance(inner_tag, Tag):
            if inner_tag.name == name and inner_tag.prefix is None:
                string: NavigableString = inner_tag.string
                if string is not None:
                    string = str(string).strip()
                    break
                else:
                    logger.warning(
                        f"Couldn`t extract content from <{inner_tag.name}> in xml, from source [{url}]"
                    )
    if string is None:
        logger.warning(
            f"Couldn`t found expected <{name}> tag within parent tag <{parent_tag.name}> in xml, from source [{url}]"
        )
    return string


def remove_tags(text: str) -> str:
    """Remove all tags from text.

    Args:
        text (str): dirty text

    Returns:
        str: cleared text
    """
    return TAG_RE.sub("", text)
