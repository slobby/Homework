# -*- coding: utf-8 -*-
"""fb2 converter module."""

from typing import List
import requests
from urllib3.exceptions import InsecureRequestWarning
from yattag import Doc, indent
from rssreader.interfaces import FeedClass, EntryClass
from rssreader.constants import ENCODING_OUT, TIMEOUT
from rssreader.app_logger import get_logger
from rssreader.errors import (
    EmptyHTTPResponseException,
    WrongXMLContetException,
    EmptyXMLTagException,
    GetFeedException,
)
import base64

logger = get_logger(__name__)


def fb2_converter(feeds: List[FeedClass], path: str) -> None:
    """Convert feeds to html.

    Args:
        feeds (List[FeedClass]): feeds
        path (str): file path
    """
    doc, tag, text, line = Doc().ttl()
    fiction_start = """<?xml version="1.0" encoding="utf-8"?>
    <FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0"
  xmlns:l="http://www.w3.org/1999/xlink">"""
    fiction_stop = "</FictionBook>"
    doc.asis(fiction_start)
    with tag("description"):
        with tag("title-info"):
            with tag("author"):
                line("first-name", "Andrew")
                line("last-name", "Shcherba")
            line("book-title", "RSS feeds")
    with tag("body"):
        for feed in feeds:
            with tag("section"):
                with tag("title"):
                    with tag("p"):
                        line("strong", feed.title)
                doc.stag("empty-line")
                with tag("p"):
                    doc.asis(
                        f"Feed source <a l:href='#{feed.source}'>{feed.source}</a>")
                with tag("p"):
                    doc.asis(f"Link: <a l:href='#{feed.link}'>{feed.link}</a>")
                if feed.description:
                    with tag("p"):
                        text("Description:")
                    line("p", feed.description)
                doc.stag("empty-line")
                for entry in feed.entries:
                    with tag("section"):
                        with tag("title"):
                            with tag("p"):
                                line("strong", entry.title)
                        line("p", f"{entry.published}")
                        with tag("p"):
                            doc.asis(
                                f"Link: <a l:href='#{entry.link}'>{entry.link}</a>")
                        if entry.description_parsed:
                            line("p", entry.description_parsed)
                        if (entry.enclosure or entry.content):
                            doc.asis(
                                f"<image l:href='#{entry.enclosure or entry.content}'/>")
                        doc.stag("empty-line")
                        doc.stag("empty-line")
    for feed in feeds:
        for entry in feed.entries:
            if (entry.enclosure or entry.content):
                img_bytes = try_get_image(entry)
                if img_bytes:
                    doc.asis(
                        f"<binary id='{entry.enclosure or entry.content}' content-type='image/jpeg'>{base64.b64encode(img_bytes).decode(ENCODING_OUT)}</binary>")
    doc.asis(fiction_stop)
    result = indent(doc.getvalue())
    with open(path, 'w', encoding=ENCODING_OUT) as f:
        f.write(result)
    return


def try_get_image(entry: EntryClass):
    result = None
    any_image_url = entry.enclosure or entry.content
    if any_image_url:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = None
        try:
            response = requests.get(
                url=any_image_url, timeout=TIMEOUT, verify=False)
            if response is None:
                raise EmptyHTTPResponseException()
        except EmptyHTTPResponseException:
            logger.error(f"Get empty response from source [{any_image_url}]")
        except requests.RequestException as ex:
            logger.error(
                f"There was an exception that occurred while handling [{any_image_url}]. Exception - {ex}"
            )
        except Exception as ex:
            logger.critical(
                f"There was unexpected exception that occurred while handling [{any_image_url}]", stack_info=True)
        else:
            result = response.content
        # raise GetFeedException(sourse=any_image_url)
    return result
