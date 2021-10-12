# -*- coding: utf-8 -*-
"""Params tuple."""


import argparse
from collections import namedtuple
import os
from constants import RSS_VERBOSE


class ProgramArgs:
    source: str = ""
    is_json: bool = False
    is_verbose: bool = False
    limit: int = -1

    def __init__(self, other: argparse.Namespace):
        self.source = other.source if "source" in other else ProgramArgs.source
        self.is_json = other.is_json if "is_json" in other else ProgramArgs.is_json
        self.is_verbose = (
            other.is_verbose if "is_verbose" in other else ProgramArgs.is_verbose
        )
        self.limit = other.limit if "limit" in other else ProgramArgs.limit

    def set_verbose_mode(self):
        os.environ[RSS_VERBOSE] = "TRUE" if self.is_verbose else "FALSE"
