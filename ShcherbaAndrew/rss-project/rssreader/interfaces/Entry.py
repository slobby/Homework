# -*- coding: utf-8 -*-
"""Entry module."""


import uuid
from typing import List


class EntryClass:
    """Describe entry of chanel."""

    def __init__(
        self,
        title: str,
        link: str,
        description: str,
        description_parsed: str,
        published: str,
        guid: str,
        enclosure: str,
        id: str = None,
    ):
        """Create entity.

        Args:
            id (string): A UUID for this feed.
            title (string): The title of the entry.
            link (string): The primary link of this entry.
            description (string): The raw value of content for this entry.
            description_parsed (string): The value of content for this entry.
            published (string): The date this entry was first published, as a string in the same format as it was published in the original feed.
        """
        self.id: str = id if id else str(uuid.uuid4())
        self.title: str = title
        self.link: str = link
        self.description: str = description
        self.description_parsed: str = description_parsed
        self.published: str = published
        self.enclosure: str = enclosure
        self.guid: str = guid if guid else str(self.id)

    def to_string(self) -> str:
        """Represent entry info as string.

        Returns:
            str: output string
        """
        return f"\n\
Title  : {self.title if self.title else ''}\n\
Link   : {self.link if self.link else ''}\n\
Date   : {self.published if self.published else ''}\n\
Media  : { self.enclosure if self.enclosure else ''}\n\
Content: {self.description_parsed if self.description_parsed else ''}\n\
\n"
