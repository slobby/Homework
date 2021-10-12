# -*- coding: utf-8 -*-
"""Getting command line params module."""


import argparse
import sys
from constants import VERSION
from interfaces import ProgramArgs


def get_args() -> ProgramArgs:
    """[summary]"""

    parser = argparse.ArgumentParser(
        description="Pure Python command-line \
RSS reader."
    )
    parser.add_argument("source", help="RSS URL")
    parser.add_argument(
        "--version",
        action="version",
        version=f"Version {VERSION}",
        help="Print version info",
    )
    parser.add_argument(
        "--json",
        dest="is_json",
        action="store_true",
        help="Print result as JSON in stdout",
    )
    parser.add_argument(
        "--verbose",
        dest="is_verbose",
        action="store_true",
        help="Outputs verbose status messages",
    )
    parser.add_argument(
        "--limit ",
        dest="limit",
        type=int,
        default=sys.maxsize,
        metavar="",
        help="Limit news topics (should be more then 0) if this parameter provided.",
    )

    args = parser.parse_args()
    programArgs = ProgramArgs(args)
    if programArgs.limit < 1:
        sys.stdout.write(f"Wrong --limit param value - [{programArgs.limit}].\n")
        parser.print_help()
        parser.exit(1)

    programArgs.set_verbose_mode()

    return programArgs
