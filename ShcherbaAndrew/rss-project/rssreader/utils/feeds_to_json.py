# -*- coding: utf-8 -*-
"""feed_to_json module."""

import json
from typing import List
from rssreader.interfaces import FeedClass


def feeds_to_json(list_of_feed: List[FeedClass]) -> str:
    """Represent list of Feeds as a JSON.

    Args:
        list_of_feed (List[FeedClass]): list of Feeds
        amount (int): amount of entries

    Returns:
        str: result JSON
    """
    JSON_list = [json.loads(i.toJson()) for i in list_of_feed]
    return json.dumps(JSON_list, indent=4, ensure_ascii=False)
