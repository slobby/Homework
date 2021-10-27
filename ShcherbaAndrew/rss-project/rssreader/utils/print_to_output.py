# -*- coding: utf-8 -*-
"""print_to_output module."""

import sys
from typing import List
from .feeds_to_json import feeds_to_json
from .feeds_to_string import feeds_to_string

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

    if params.is_json:
        file.write(feeds_to_json(list_of_feed))
    else:
        file.write(feeds_to_string(list_of_feed))
    return
