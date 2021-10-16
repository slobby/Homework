# -*- coding: utf-8 -*-
"""Feed module."""

import json
import time
import uuid
import jsonpickle
from typing import List
from .Image import ImageClass
from .Entry import EntryClass

jsonpickle.set_preferred_backend("json")
jsonpickle.set_encoder_options("json", ensure_ascii=False)


class FeedClass:
    """Describe chanel."""

    def __init__(
        self,
        title: str,
        link: str,
        image: ImageClass,
        description: str,
        published: str,
        published_parsed: time.struct_time,
        entries: List[EntryClass],
        id: uuid.UUID = None,
    ):
        """Create entity.

        Args:
            id (uuid.UUID): A UUID for this feed.
            title (string): The title of the feed.
            link (string): The primary link of this feed.
            image ()
            description (string): The value of description for this entry.
            published (string): The date this entry was first published, as a string in the same format as it was published in the original feed.
            published_parsed (time.struct_time): The date this entry was first published, as a standard Python 9-tuple.
            entries (List[Entry]): A list of Entries
        """
        self.id: uuid.UUID = id if id else uuid.uuid4()
        self.title: str = title
        self.link: str = link
        self.image: ImageClass = image
        self.description: str = description
        self.published: str = published
        self.published_parsed: time.struct_time = published_parsed
        self.entries: List[EntryClass] = entries

    def to_string(self) -> str:
        """Represent main feed info as string.

        Returns:
            str: output string
        """
        result = f"\n\n\
Feed: {self.title if self.title else ''}\n\n\
Link: {self.link if self.link else ''}\n\
Date: {self.published if self.published else ''}\n\
Description: {self.description if self.description else ''}\n\
Image: {self.image if self.image else ''}\n\n\n"

        for index, value in enumerate(self.entries):
            result += f"\nNews [{index+1}]\n{value.to_string()}"

        return result

    def toJson(self) -> str:
        """Encode to JSON.

        Returns:
            str: JSON object
        """
        return jsonpickle.encode(self, unpicklable=False)
