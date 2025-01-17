# -*- coding: utf-8 -*-
"""feed_to_string module."""

import sys
from typing import List
from rssreader.interfaces import FeedClass


def feeds_to_string(list_of_feed: List[FeedClass]) -> str:
    """Represent list of Feeds as a string.

    Args:
        list_of_feed (List[FeedClass]): list of Feeds

    Returns:
        str: result string
    """
    result = ""
    for feed in list_of_feed:
        result += feed.to_string()
    return result
