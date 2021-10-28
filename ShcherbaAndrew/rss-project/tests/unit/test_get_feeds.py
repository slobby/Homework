# -*- coding: utf-8 -*-
"""Test get_feeds functions."""

import sys
from bs4 import BeautifulSoup
from rssreader.get_feeds import get_feed_from_URL, remove_tags, extract_atr_from_tag, extract_string_from_tag
from rssreader.command_line_parser import get_args
from rssreader.interfaces import FeedClass


def test_remove_tags_return_cleared_string():
    input_string = "<a>test string</a>"
    expected_string = "test string"
    assert remove_tags(input_string) == expected_string


def test_extract_atr_from_tag_return_None():
    soup = BeautifulSoup()
    new_parent_tag = soup.new_tag("channel")
    new_link = soup.new_tag('a', href="mock.site.com")
    new_parent_tag.append(new_link)

    assert extract_atr_from_tag(new_parent_tag, "a", "url", "fake") == None


def test_extract_atr_from_tag_return_atr():
    soup = BeautifulSoup()
    new_parent_tag = soup.new_tag("channel")
    new_link = soup.new_tag('a', href="mock.site.com")
    new_parent_tag.append(new_link)
    assert extract_atr_from_tag(
        new_parent_tag, "a", "href", "fake") == "mock.site.com"


def test_extract_string_from_tag_return_None():
    soup = BeautifulSoup()
    new_parent_tag = soup.new_tag("channel")
    new_title = soup.new_tag('nottitle')
    new_title.string = "not expected"
    new_parent_tag.append(new_title)
    assert extract_string_from_tag(
        new_parent_tag, "title", "fake") == None


def test_extract_string_from_tag_return_string():
    soup = BeautifulSoup()
    new_parent_tag = soup.new_tag("channel")
    new_title = soup.new_tag('title')
    new_title.string = "expected"
    new_parent_tag.append(new_title)
    assert extract_string_from_tag(
        new_parent_tag, "title", "fake") == "expected"


def test_get_feed_from_URL():
    args_list = ["test",
                 "https://www.dotabuff.com/blog.rss"]
    sys.argv = args_list
    args = get_args()
    res = get_feed_from_URL(args)
    assert type(res) == FeedClass
