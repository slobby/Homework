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

    def __init__(self, message=None, sourse=None):

        self.message = (
            message
            if message
            else f"Error. While parsing xml from [{sourse}] the error has occured. \
See log or use --verbose mode"
        )


class GetFeedException(Exception):
    """GetFeedException exception."""

    def __init__(self, message=None, sourse=None):

        self.message = (
            message
            if message
            else f"Error. While fetching [{sourse}] the error has occured. \
See log or use --verbose mode"
        )
