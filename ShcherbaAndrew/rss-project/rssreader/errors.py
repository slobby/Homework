# -*- coding: utf-8 -*-
"""Errors module."""


class EmptyHTTPResponseException(Exception):
    """EmptyHTTPResponseException exception."""

    pass


class EmptyXMLTagException(Exception):
    """EmptyHTTPResponseException exception."""

    pass


class WrongXMLContetException(Exception):
    """WrongXMLContetException exception."""

    def __init__(self, message=None, source=None):

        self.message = (
            message
            if message
            else f"Error. While parsing xml from [{source}] the error has occured. \
See log or use --verbose mode"
        )


class GetFeedException(Exception):
    """GetFeedException exception."""

    def __init__(self, message=None, source=None):

        self.message = (
            message
            if message
            else f"Error. While fetching [{source}] the error has occured. \
See log or use --verbose mode"
        )


class ZeroFeedAmountException(Exception):
    """ZeroFeedAmountException exception."""

    def __init__(self, message=None, source=None):

        self.message = (
            message
            if message
            else f"Error. The amount of news is 0. From source [{source}]"
        )


class ZeroLimitAmountException(Exception):
    """ZeroLimitAmountException exception."""

    def __init__(self, message=None, source=None):

        self.message = (
            message
            if message
            else f"Due you set '--limit' to 0, the result is null."
        )
