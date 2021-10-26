# -*- coding: utf-8 -*-
"""print_to_output module."""

import sys
from typing import List
from .feeds_to_json import feeds_to_json
from .feeds_to_string import feeds_to_string
from .trunc_feed_list import trunc_feed_list

from rssreader.interfaces import FeedClass, ProgramArgs
from rssreader.errors import ZeroLimitAmountException


def print_to_output(
    list_of_feed: List[FeedClass], params: ProgramArgs, file=None
) -> None:
    """Write feeds in filedescriptor.

    Args:
        list_of_feed (List[FeedClass]): List of FeedClass entities
        params (ProgramArgs): command line params
    """
    if file is None:
        file = sys.stdout

    if params.limit == 0:
        raise ZeroLimitAmountException
    total_news_amount = sum((len(item.entries) for item in list_of_feed), 0)

    news_amount = (
        params.limit
        if params.limit is not None and params.limit < total_news_amount
        else total_news_amount
    )
    if news_amount == 0:
        file.write("Error. The amount of news is 0.")
        return

    trunced_list_of_feed = trunc_feed_list(list_of_feed, news_amount)

    if params.is_json:
        file.write(feeds_to_json(trunced_list_of_feed))
    else:
        file.write(feeds_to_string(trunced_list_of_feed))
    return
