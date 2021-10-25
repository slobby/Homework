# -*- coding: utf-8 -*-
"""html converter module."""

from typing import List
from yattag import Doc, indent
from rssreader.interfaces import FeedClass
from rssreader.constants import ENCODING_OUT


def html_converter(feeds: List[FeedClass], path: str) -> None:
    """Convert feeds to html.

    Args:
        feeds (List[FeedClass]): feeds
        path (str): file path
    """
    doc, tag, text, line = Doc().ttl()
    head_tag = '''<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>RSS reader</title>
</head>'''

    doc.asis("<!DOCTYPE html>")
    with tag("html", lang="en"):
        doc.asis(head_tag)
        with tag("body"):
            with tag("div"):
                for feed in feeds:
                    with tag("div"):
                        line("h1", "Feed", klass="display-4")
                        line("p", feed.title, klass="lead")
                        with tag("p", klass="lead"):
                            line("a", "feed source", href=feed.source)
                        with tag("p", klass="lead"):
                            line("a", "link", href=feed.link)
                        if feed.description:
                            with tag("p", klass="lead"):
                                text("description :")
                            line("p", feed.description)
                        doc.stag("hr", klass="my-1")
                        with tag("div"):
                            for entry in feed.entries:
                                with tag("div", style="outline: 2px solid"):
                                    line("h3", entry.title, klass="lead")
                                    line(
                                        "p", f"date: {entry.published}", klass="lead")
                                    with tag("p", klass="lead"):
                                        line("a", "link", href=entry.link)
                                    if (entry.enclosure):
                                        with tag("div"):
                                            doc.stag(
                                                "img", src=entry.enclosure, height="200", width="200")
                                    if entry.description:
                                        line("p", "description :", klass="lead")
                                        with tag("p", klass="lead"):
                                            doc.asis(entry.description)

    result = indent(doc.getvalue())
    with open(path, 'w', encoding=ENCODING_OUT) as f:
        f.write(result)
    return
