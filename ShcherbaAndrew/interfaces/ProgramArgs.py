# -*- coding: utf-8 -*-
"""Params module."""


import argparse
import os
import time
from constants import RSS_VERBOSE


class ProgramArgs:
    """Represent all command-line properties."""

    source: str = ""
    is_json: bool = False
    is_verbose: bool = False
    limit: int = -1
    date: time.struct_time = None

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
        self.limit = other.limit if "limit" in other else ProgramArgs.limit
        self.date = other.date if "date" in other else ProgramArgs.date

    def set_verbose_mode(self):
        """Set enviroment property RSS_VERBOSE."""
        os.environ[RSS_VERBOSE] = "TRUE" if self.is_verbose else "FALSE"
