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
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <style>
    /*Обнуление*/
    * {
      padding: 0;
      margin: 0;
      border: 0;
    }

    *,
    *:before,
    *:after {
      -moz-box-sizing: border-box;
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
    }

    :focus,
    :active {
      outline: none;
    }

    a:focus,
    a:active {
      outline: none;
    }

    nav,
    footer,
    header,
    aside {
      display: block;
    }

    html,
    body {
      height: 100%;
      width: 100%;
      font-size: 100%;
      line-height: 1;
      font-size: 14px;
      -ms-text-size-adjust: 100%;
      -moz-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
    }

    input,
    button,
    textarea {
      font-family: inherit;
    }

    input::-ms-clear {
      display: none;
    }

    button {
      cursor: pointer;
    }

    button::-moz-focus-inner {
      padding: 0;
      border: 0;
    }

    a,
    a:visited {
      text-decoration: none;
    }

    a:hover {
      text-decoration: none;
    }

    ul li {
      list-style: none;
    }

    img {
      vertical-align: top;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      font-size: inherit;
      font-weight: inherit;
    }

    /*--------------------*/
    body {
      font-family: Arial, Helvetica, sans-serif;
    }

    .wrapper {
      min-height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;

    }

    .content {
      flex: 1 1 auto;
      max-width: 1180px;
      margin: auto;
    }

    .cotainer {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .feed__head {
      background-color: #b1bbc7;
      margin: 0px auto;
      padding: 20px;
      color: #fdfdfd;
      font-size: 20px;
      letter-spacing: 0.3px;
    }

    .feed__head p {
      font-size: 14px;
      margin: 10px 0px;
    }

    .feed__head__title {
      color: #fdfdfd;

    }

    .feed__header__date {
      font-size: 14px;
      margin: 10px 0px;
    }

    .feed__items {
      color: #445161;
      display: flex;
      flex-direction: column;
      margin: 20px 0px;
    }

    .feed__item {
      display: flex;
      background-color: #f5f5f5;
      margin: 10px 0px;
    }

    .feed__item__info {
      padding: 20px;
      flex: 4;
    }

    .feed__item__info p {
      font-size: 14px;
      margin: 10px 0px;
    }

    .feed__item__title {
      font-size: 16px;
    }

    .feed__item__image {
      padding: 20px;
      flex: 1;
    }
    
    img{
        max-width: 100%;
        max-height: 100%;
        display: block; /* remove extra space below image */
    }

    .footer {
      background-color: #f5f5f5;
      flex: 0 0 auto;
    }

    .footer__row {
      display: flex;
      height: 65px;
      justify-content: center;
      align-items: center;
    }

    .footer__text {
      color: #445162;
      font-size: 12px;
      letter-spacing: 0.3px;
    }
  </style>
  <title>RSS reader</title>
</head>'''

    footer = '''
    <footer class="footer">
        <div class="footer__container">
            <div class="footer__row">
            <div class="footer__text">RSS News 2021</div>
            </div>
        </div>
        </footer>'''

    doc.asis("<!DOCTYPE html>")
    with tag("html", lang="en"):
        doc.asis(head_tag)
        with tag("body"):
            with tag("div", klass="wrapper"):
                with tag("div", klass="content"):
                    with tag("div", klass="container"):
                        for feed in feeds:
                            with tag("div", klass="feed"):
                                with tag("div", klass="feed__head"):
                                    line("div", feed.title,
                                         klass="feed__head__title")
                                    with tag("p"):
                                        line("a", feed.source,
                                             href=feed.source)
                                    with tag("p",):
                                        line("a", feed.link, href=feed.link)
                                    if feed.description:
                                        with tag("p"):
                                            line("p", feed.description)
                                with tag("div", klass="feed__items"):
                                    for entry in feed.entries:
                                        with tag("div", klass="feed__item"):
                                            with tag("div", klass="feed__item__info"):
                                                line("div", entry.title,
                                                     klass="feed__item__title")
                                                line("p", f"{entry.published}")
                                                with tag("p"):
                                                    line("a", entry.link,
                                                         href=entry.link)
                                                if entry.description:
                                                    with tag("p"):
                                                        doc.asis(
                                                            entry.description)
                                            with tag("div", klass="feed__item__image"):
                                                if (entry.enclosure or entry.content or entry.thumbnail):
                                                    doc.stag(
                                                        "img", src=(entry.enclosure or entry.content or entry.thumbnail))
            doc.asis(footer)
    result = indent(doc.getvalue())
    with open(path, 'w', encoding=ENCODING_OUT) as f:
        f.write(result)
    return
