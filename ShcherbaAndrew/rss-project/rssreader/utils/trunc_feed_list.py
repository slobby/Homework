# -*- coding: utf-8 -*-
"""trunc feed list module."""

from typing import List
from rssreader.interfaces import FeedClass, ProgramArgs


def trunc_feed_list(list_of_feed: List[FeedClass], amount: int) -> List[FeedClass]:
    """Reduce total amount of entries in all feeds to passed value.

    Args:
        list_of_feed (List[FeedClass]): list of Feeds
        amount (int): amount of entries

    Returns:
        List[FeedClass]: list of Feeds
    """
    inner_amount = amount
    result = []
    for feed in list_of_feed:
        length = len(feed.entries)
        if inner_amount <= length:
            feed.entries = feed.entries[:inner_amount]
            result.append(feed)
            break
        else:
            result.append(feed)
        inner_amount -= length
    return result
