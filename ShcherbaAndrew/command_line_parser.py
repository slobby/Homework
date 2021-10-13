# -*- coding: utf-8 -*-
"""Getting command line params module."""


import argparse
import sys
from constants import VERSION
from interfaces import ProgramArgs
from interfaces import date_type


def get_args() -> ProgramArgs:
    """Get command line properties.

    Returns:
        ProgramArgs: An instance of ProgramArgs
    """
    parser = argparse.ArgumentParser(
        description="Pure Python command-line \
RSS reader."
    )
    parser.add_argument("source", nargs="?", default=None, help="RSS URL")
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
        default=None,
        metavar="",
        help="Limit news topics (should be more then 0) if this parameter provided.",
    )

    parser.add_argument(
        "--date ",
        dest="date",
        default=None,
        type=date_type,
        metavar="",
        help="Specify actual publishing date (should be in format earmonthday [20211005]) if this parameter provided.",
    )

    args = parser.parse_args()
    programArgs = ProgramArgs(args)
    if programArgs.limit is not None and programArgs.limit < 1:
        sys.stdout.write(f"Wrong --limit param value - [{programArgs.limit}].\n")
        parser.print_help()
        parser.exit(1)
    if programArgs.source is None and programArgs.date is None:
        sys.stdout.write(
            f"Param [sourse] is required if you don`t set param [--date].\n"
        )
        parser.print_help()
        parser.exit(1)

    programArgs.set_verbose_mode()

    return programArgs
