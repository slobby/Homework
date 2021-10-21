import os
import json

from datetime import datetime, date, time, timezone
from typing import Any, Callable, List, Union
from rssreader.utils import date_type
import copy
import pickle

from rssreader.interfaces import FeedClass, EntryClass




class DBService():

    def __init__(self, file: str) -> None:
        self.file = file
        if not os.path.isfile(self.file):
            self.seeds()

    def insert(self, feeds: List[FeedClass])-> None:
        outer_feeds = copy.deepcopy(feeds)
        with open(self.file, 'rb') as f:
            inner_feeds= pickle.load(f)
        if inner_feeds:
            for _ in range(len(outer_feeds)):
                outer_feed = outer_feeds.pop()
                for inner_feed in inner_feeds:
                    if outer_feed.link==inner_feed.link:
                        guid_set={entry.guid for entry in inner_feed.entries}
                        filtred_entries = list(filter(lambda x: x.guid not in guid_set, outer_feed))
                        inner_feed.entries.extend(filtred_entries)
                        break                        
                else:
                    inner_feeds.append(outer_feed)
        else:
            inner_feeds.extend(feeds)

        with open(self.file, 'wb') as f:
            pickle.dump(inner_feeds, f)

    def find_all(self) -> List[FeedClass]:
        with open(self.file, 'rb') as f:
            inner_feeds = pickle.load(f)
        return inner_feeds
    
    
    def find_by_date(self, feeds: List[FeedClass], date: time.struct_time) -> List[FeedClass]:
        result=[]
        for feed in feeds:
            filtered_feed = self.date_filter(feed, date)
            if filtered_feed:
                result.append(filtered_feed)
        return result
                
    




    def url_filter(self, feed: FeedClass, url: str) -> Union[FeedClass, None]:

        
        if feed.url==url:
            feed.entries = filtered_entries
        else:
            return None
        return feed

        
    
    def date_filter(self, feed: FeedClass, date: time.struct_time) -> Union[FeedClass, None]:
        filtered_entries=[]
        for entry in feed.entries:
            entry_date = date_type(entry.published)
            if (entry_date and entry_date.tm_year == date.tm_year and entry_date.tm_mon == date.tm_mon and entry_date.tm_mday == date.tm_mday):
                filtered_entries.append(entry)
        if filtered_entries:
            feed.entries = filtered_entries
        else:
            return None
        return feed
                
            
        
                

        
                        

    # def read_url(self, url: str, date_filter: str, limit: int = None) -> Feed:
    #     """[Read data only specified url]
    #     Args:
    #         url (str): [link]
    #         date_filter (str): [for the specified date]
    #         limit (int, optional): [no more records if Nonenthen all]. Defaults to None.
    #     Raises:
    #         ExceptionFormatDate: [Invalid data format]
    #         ExceptionNotFoudNewsDate: [no data for such date or link]
    #     Returns:
    #         Feed: [Found data from RSS]
    #     """
    #     try:
    #         datetime.strptime(date_filter, '%Y%m%d')
    #     except Exception:
    #         raise ExceptionFormatDate("Incorrect data format, should be %Y%m%d")
    #     with open(self._path, 'rb') as f:
    #         feeds_storage = pickle.load(f)

    #     def equal_date(item: Item) -> bool:
    #         dt = parse(item.date)
    #         dt_str = f'{dt.year}{dt.month}{dt.day}'
    #         if dt_str == date_filter:
    #             return True
    #         else:
    #             return False
    #     _, find_in_storage = next(((idx, feed) for idx, feed in enumerate(
    #         feeds_storage.feeds) if feed.url == url), (None, None))

    #     if find_in_storage is not None:
    #         find_news_date = [item for item in find_in_storage.items if equal_date(item)]
    #         return Feed(find_in_storage.url, find_in_storage.feed_title, find_news_date[:limit])
    #     else:
    #         raise ExceptionNotFoudNewsDate(f'Is not news {url}')

    # def read_all(self, filter_date: str, limit: int = None) -> ListFeeds:
    #     """[[Read data all url feeds]]
    #     Args:
    #         filter_date (str): [for the specified date]
    #         limit (int, optional): [no more records if Nonenthen all]. Defaults to None.
    #     Raises:
    #         ExceptionNotFoudNewsDate: [no data for such link]
    #     Returns:
    #         ListFeeds: [Found list data from RSS]
    #     """
    #     result = ListFeeds(list())
    #     with open(self._path, 'rb') as f:
    #         feeds_storage = pickle.load(f)
    #     for item_feed in feeds_storage.feeds:
    #         feed = self.read_url(item_feed.url, filter_date, limit)
    #         if len(feed.items) != 0:
    #             result.feeds.append(feed)
    #     if len(result.feeds) == 0:
    #         raise ExceptionNotFoudNewsDate(f'Is not news in {filter_date}')

    #     return result


    def seeds(self):
        with open(self.file, 'wb') as f:
                pickle.dump([], f)