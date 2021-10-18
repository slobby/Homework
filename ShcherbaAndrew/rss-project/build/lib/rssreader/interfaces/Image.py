# -*- coding: utf-8 -*-
"""Image module."""


import json


class ImageClass:
    """Describe image of chanel."""

    def __init__(
        self,
        title: str,
        url: str,
        link: str,
        width: str,
        height: str,
        description: str,
    ):
        """Create image.

        Args:
            title (string): The title of the image.
            url (string): The URL which the feed image would point to.
            link (string): The URL of the feed image itself.
            width (str): The width of the feed image.
            height (str): The height of the feed image.
            description (string): A short description of the feed image.
        """
        self.title: str = title
        self.url: str = url
        self.link: str = link
        self.width: str = width
        self.height: str = height
        self.description: str = description

    def __str__(self) -> str:
        """Represent instance as string.

        Returns:
            str: output string
        """
        return self.url if self.url else ""
