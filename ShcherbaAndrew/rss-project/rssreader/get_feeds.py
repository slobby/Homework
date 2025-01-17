# -*- coding: utf-8 -*-
"""date_type module."""

from typing import List, Union
from bs4.element import NavigableString, Tag
from rssreader.app_logger import get_logger
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from rssreader.errors import (
    EmptyHTTPResponseException,
    WrongXMLContetException,
    EmptyXMLTagException,
    GetFeedException,
)
from rssreader.interfaces import ProgramArgs, EntryClass, FeedClass, DBService
from rssreader.utils.trunc_feed_list import trunc_feed_list
from rssreader.constants import TIMEOUT, TAG_RE

logger = get_logger(__name__)


def get_feeds(params: ProgramArgs) -> List[FeedClass]:
    """Get feeds.

    Args:
        params (ProgramArgs): command line params

    Returns:
        List[FeedClass]: List of FeedClass entities
    """
    db_service = DBService()
    feeds = []
    if params.date is None:
        feeds.append(get_feed_from_URL(params))
        db_service.insert(feeds)
    else:
        feeds.extend(get_feed_from_storage(db_service, params))

    total_news_amount = sum((len(item.entries) for item in feeds), 0)

    news_amount = (
        params.limit
        if params.limit is not None and params.limit < total_news_amount
        else total_news_amount
    )
    if news_amount != 0:
        feeds = trunc_feed_list(feeds, news_amount)
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
        response = requests.get(
            url=params.source, timeout=TIMEOUT, verify=False, headers={'User-agent': 'rss-reader'})
        if response is None:
            raise EmptyHTTPResponseException()
    except EmptyHTTPResponseException:
        logger.error(f"Get empty response from source [{params.source}]")
    except requests.RequestException as ex:
        logger.error(
            f"There was an exception that occurred while handling [{params.source}]. Exception - {ex}"
        )
    except Exception as ex:
        logger.critical(
            f"There was unexpected exception that occurred while handling [{params.source}]", stack_info=True)
    else:
        return parse_to_feed(response)
    raise GetFeedException(sourse=params.source)


def get_feed_from_storage(db: DBService, params: ProgramArgs) -> List[FeedClass]:
    """Get feeds from storage.

    Args:
        db (DBService): DB service
        params (ProgramArgs): app params

    Returns:
        (List[FeedClass]): feeds
    """
    result = DBService.find_by_date(db.find_all(), params.date)
    if params.date and params.source:
        return DBService.find_by_url(result, params.source)
    else:
        return result


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
        description = extract_string_from_tag(
            channel_tag, "description", req.url)
        entries = parse_items(channel_tag.find_all("item"), req.url)
        feed = FeedClass(
            source=req.url,
            title=title,
            link=link,
            description=description,
            entries=entries,
        )
    except EmptyXMLTagException:
        logger.error(
            f"Couldn`t found <chanel> tag in xml, from source [{req.url}]")
    else:
        return feed
    raise WrongXMLContetException(sourse=req.url)


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
            if title:
                title = remove_tags(title)
            link = extract_string_from_tag(item, "link", req_url)
            description = extract_string_from_tag(item, "description", req_url)
            description_parsed = None
            if description:
                description_parsed = remove_tags(description)
            published = extract_string_from_tag(item, "pubDate", req_url)
            guid = extract_string_from_tag(item, "guid", req_url)
            enclosure = extract_atr_from_tag(item, "enclosure", "url", req_url)
            content = extract_atr_from_tag(item, "content", "url", req_url)
            thumbnail = extract_atr_from_tag(item, "thumbnail", "url", req_url)

            entry = EntryClass(
                title=title,
                link=link,
                description=description,
                description_parsed=description_parsed,
                published=published,
                guid=guid,
                enclosure=enclosure,
                content=content,
                thumbnail=thumbnail
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
            f"Couldn`t found expected <{name}> tag withing parent tag <{parent_tag.name}> in xml, from source [{url}]"
        )
    return string


def extract_atr_from_tag(parent_tag: Tag, name: str, atr: str, url: str) -> Union[str, None]:
    """Exctract Atribute from Tag, and convert to unicode.

    Args:
        parent_tag (Tag): parent tag
        name (str): suggested tag name
        url (str): xml url

    Returns:
        Union[str, None]: exctracted string, or None if couldn`t exctracted, or target_tag is None
    """
    atribute = None
    # target_tags = parent_tag.find_all(name)
    for inner_tag in parent_tag.children:
        if isinstance(inner_tag, Tag):
            if inner_tag.name == name:
                atribute = inner_tag.get(atr, None)
                if atribute is not None:
                    is_jpeg = atribute.endswith("image/jpeg")
                if atribute is not None and is_jpeg:
                    break
                else:
                    logger.warning(
                        f"Couldn`t extract content from <{inner_tag.name}> in xml, from source [{url}]"
                    )
    if atribute is None:
        logger.warning(
            f"Couldn`t found expected [{atr}] atribute in <{name}> tag within parent tag <{parent_tag.name}> in xml, from source [{url}]"
        )
    return atribute


def remove_tags(text: str) -> str:
    """Remove all tags from text.

    Args:
        text (str): dirty text

    Returns:
        str: cleared text
    """
    return TAG_RE.sub("", text)
