# -*- coding: utf-8 -*-
"""DBService module."""

import os
import time
import copy
import pickle
from typing import Any, Callable, List, Union
from rssreader.utils import date_type
from rssreader.interfaces import FeedClass
from rssreader.constants import DB_FILE, DB_DIR


class DBService():
    """Describe database service class."""

    def __init__(self, file: str = None) -> None:
        """Init new DBService instance.

        Args:
            file (str): Database path
        """
        if not file:
            db_dir = os.path.join(os.path.dirname(
                os.path.dirname(__file__)), DB_DIR)
            if not os.path.isdir(db_dir):
                os.mkdir(db_dir)
            file = os.path.join(db_dir, DB_FILE)
        self.file = file
        if not os.path.isfile(self.file):
            self.seeds()

    def seeds(self):
        """Seed new database."""
        with open(self.file, 'wb') as f:
            pickle.dump([], f)

    def insert(self, feeds: List[FeedClass]) -> None:
        """Insert list of feeds.

        Args:
            feeds (List[FeedClass]): feeds
        """
        outer_feeds = copy.deepcopy(feeds)
        with open(self.file, 'rb') as f:
            inner_feeds = pickle.load(f)
        if inner_feeds:
            for _ in range(len(outer_feeds)):
                outer_feed = outer_feeds.pop()
                for inner_feed in inner_feeds:
                    if outer_feed.link == inner_feed.link:
                        guid_set = {entry.guid for entry in inner_feed.entries}
                        filtred_entries = list(
                            filter(lambda x: x.guid not in guid_set, outer_feed.entries))
                        inner_feed.entries.extend(filtred_entries)
                        break
                else:
                    inner_feeds.append(outer_feed)
        else:
            inner_feeds.extend(feeds)

        with open(self.file, 'wb') as f:
            pickle.dump(inner_feeds, f)

    def find_all(self) -> List[FeedClass]:
        """Get all from db.

        Returns:
            List[FeedClass]: feeds
        """
        with open(self.file, 'rb') as f:
            inner_feeds = pickle.load(f)
        return inner_feeds

    @staticmethod
    def find_by_date(feeds: List[FeedClass], date: time.struct_time) -> List[FeedClass]:
        """Find by date.

        Args:
            feeds (List[FeedClass]): feeds
            date (time.struct_time): date condition

        Returns:
            List[FeedClass]: filtered feeds
        """
        @filter_init(date)
        def date_filter(feed: FeedClass, date: time.struct_time) -> Union[FeedClass, None]:
            """Feed filter by date.

            Args:
                feed (FeedClass): feed
                date (time.struct_time): date condition

            Returns:
                Union[FeedClass, None]: filtered feed
            """
            filtered_entries = []
            for entry in feed.entries:
                entry_date = date_type(
                    entry.published, "%a, %d %b %Y %H:%M:%S %z")
                if (entry_date and entry_date.tm_year == date.tm_year
                    and entry_date.tm_mon == date.tm_mon
                        and entry_date.tm_mday == date.tm_mday):
                    filtered_entries.append(entry)
            if filtered_entries:
                feed.entries = filtered_entries
            else:
                return None
            return feed

        return DBService.find_by_filter(feeds, date_filter)

    @staticmethod
    def find_by_url(feeds: List[FeedClass], source: str) -> List[FeedClass]:
        """Find by url.

        Args:
            feeds (List[FeedClass]): feeds
            source (str): url condition

        Returns:
            List[FeedClass]: feeds
        """

        @filter_init(source)
        def url_filter(feed: FeedClass, sourse: str) -> Union[FeedClass, None]:
            """Feed filter by url.

            Args:
                feed (FeedClass): feeds
                sourse (str): url condition

            Returns:
                Union[FeedClass, None]: feeds
            """
            if feed.source == sourse or \
                    feed.link == sourse or \
                    feed.source.startswith(sourse):
                return feed
            else:
                return None

        return DBService.find_by_filter(feeds, url_filter)

    @staticmethod
    def find_by_filter(feeds: List[FeedClass], filter_func: Callable) -> List[FeedClass]:
        """Filter by taken filter.

        Args:
            feeds (List[FeedClass]): feeds
            filter (Callable): filter function

        Returns:
            List[FeedClass]: feeds
        """
        result = []
        for feed in feeds:
            filtered_feed = filter_func(feed)
            if filtered_feed:
                result.append(filtered_feed)
        return result


def filter_init(cond: Any):
    """Init filter.

    Args:
        cond (Any): filter condition
    """
    def decor(func):
        def wraper(feed: FeedClass):
            return func(feed, cond)
        return wraper
    return decor
