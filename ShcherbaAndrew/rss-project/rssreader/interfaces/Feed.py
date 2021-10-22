# -*- coding: utf-8 -*-
"""Feed module."""

import uuid
import jsonpickle
from typing import List
from .Entry import EntryClass

jsonpickle.set_preferred_backend("json")
jsonpickle.set_encoder_options("json", ensure_ascii=False)


class FeedClass:
    """Describe chanel."""

    def __init__(
        self,
        source: str,
        title: str,
        link: str,
        description: str,
        entries: List[EntryClass],
        id: str = None,
    ):
        """Create entity.

        Args:
            id (string): A UUID for this feed.
            title (string): The title of the feed.
            link (string): The primary link of this feed.
            description (string): The value of description for this entry.
            entries (List[Entry]): A list of Entries
            source (str): raw source
        """
        self.id: str = id if id else str(uuid.uuid4())
        self.source: str = source
        self.title: str = title
        self.link: str = link
        self.description: str = description
        self.entries: List[EntryClass] = entries

    def to_string(self) -> str:
        """Represent main feed info as string.

        Returns:
            str: output string
        """
        result = f"\n\n\
Title: {self.title if self.title else ''}\n\n\
Link: {self.link if self.link else ''}\n\
Description: {self.description if self.description else ''}\n\n\n"

        for index, value in enumerate(self.entries):
            result += f"\nNews [{index+1}]\n{value.to_string()}"

        return result

    def toJson(self) -> str:
        """Encode to JSON.

        Returns:
            str: JSON object
        """
        return jsonpickle.encode(self, unpicklable=False)
