# -*- coding: utf-8 -*-
"""Getting command line params module."""


import argparse
import os
import time
from typing import Callable
from rssreader.constants import VERSION
from rssreader.interfaces import ProgramArgs
from rssreader.utils import print_message


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
        help="print version info",
    )
    parser.add_argument(
        "--json",
        dest="is_json",
        action="store_true",
        help="print result as JSON in stdout",
    )
    parser.add_argument(
        "--verbose",
        dest="is_verbose",
        action="store_true",
        help="outputs verbose status messages",
    )
    parser.add_argument(
        "--limit ",
        dest="limit",
        type=int,
        default=None,
        metavar="",
        help="limit news topics (should be more or equal to 0) if this parameter provided.",
    )

    parser.add_argument(
        "--date ",
        dest="date",
        default=None,
        type=lambda s: time.strptime(s, "%Y%m%d"),
        metavar="",
        help="specify actual publishing date (should be in format yearmonthday [20211005]) if this parameter provided.",
    )

    parser.add_argument(
        "--to-html ",
        dest="to_html",
        default=None,
        type=check_path_html_ext,
        metavar="",
        help="set (path)filename of created html file.",
    )

    parser.add_argument(
        "--to-fb2 ",
        dest="to_fb2",
        default=None,
        type=check_path_fb2_ext,
        metavar="",
        help="set (path)filename of created fb2 file.",
    )

    parser.add_argument(
        "--colorize",
        dest="is_colorize",
        action="store_true",
        help="colorize outputs",
    )

    args = parser.parse_args()
    programArgs = ProgramArgs(args)
    if programArgs.limit is not None and programArgs.limit < 0:
        print_message(f"Wrong --limit param value - [{programArgs.limit}].\n")
        parser.print_help()
        parser.exit(1)
    if programArgs.source is None and programArgs.date is None:
        print_message(
            f"Param [source] is required if you don`t set param [--date].\n")
        parser.print_help()
        parser.exit(1)

    return programArgs


def check_path(ext: str, path: str) -> str:
    """Check path.

    Args:
        path (str): path to file

    Raises:
        ValueError: wrong path

    Returns:
        str: absolute path
    """
    if path:
        abs_path = os.path.abspath(path)
        _, file = os.path.split(abs_path)
        if file.endswith(f".{ext}"):
            if os.path.isdir(os.path.dirname(abs_path)):
                return abs_path
        else:
            print_message(
                f"Error! Input filename [{file}] has to have '.{ext}' extention.\n")
            raise ValueError
    else:
        print_message(f"Error! Set (path)filename for output {ext} file.\n")
        raise ValueError


def check_path_set_ext(ext: str):
    """Create decorator for check path function.

    Args:
        ext (str): file extention
    """
    def decorator(func: Callable):
        def warapper(*args, **kwargs):
            return func(ext, *args, **kwargs)
        return warapper
    return decorator


check_path_html_ext = check_path_set_ext("html")(check_path)
check_path_fb2_ext = check_path_set_ext("fb2")(check_path)
