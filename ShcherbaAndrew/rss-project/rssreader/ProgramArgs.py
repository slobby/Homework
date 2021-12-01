# -*- coding: utf-8 -*-
"""Params module."""


import argparse
import os
import time
from rssreader.constants import RSS_VERBOSE, RSS_COLORIZE


class ProgramArgs:
    """Represent all command-line properties."""

    source: str = ""
    is_json: bool = False
    is_verbose: bool = False
    is_colorize: bool = False
    limit: int = None
    date: time.struct_time = None
    to_html: str = "default.html"
    to_fb2: str = "default.fb2"

    def __init__(self, other: argparse.Namespace):
        """Initialise new ProgramArgs.

        Args:
            other (argparse.Namespace): the object reterned by ArgumentParser.parse_args
        """
        self.source = other.source if "source" in other else ProgramArgs.source
        self.is_json = other.is_json if "is_json" in other else ProgramArgs.is_json
        self.is_verbose = (
            other.is_verbose if "is_verbose" in other else ProgramArgs.is_verbose
        )
        self.is_colorize = other.is_colorize if "is_colorize" in other else ProgramArgs.is_colorize
        self.limit = other.limit if "limit" in other else ProgramArgs.limit
        self.date = other.date if "date" in other else ProgramArgs.date
        self.to_html = other.to_html if "to_html" in other else ProgramArgs.to_html
        self.to_fb2 = other.to_fb2 if "to_fb2" in other else ProgramArgs.to_html
        self.set_env()

    def set_env(self):
        """Set enviroment property RSS_VERBOSE."""
        os.environ[RSS_VERBOSE] = "TRUE" if self.is_verbose else "FALSE"
        os.environ[RSS_COLORIZE] = "TRUE" if self.is_colorize else "FALSE"
