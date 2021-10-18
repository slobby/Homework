# -*- coding: utf-8 -*-
"""print_message module."""

import sys


def print_message(message: str, file=None) -> None:
    """Write message in filedescriptor.

    Args:
        message (str): message
        file ([type], optional): filedescriptor. Defaults to None.
    """
    if message:
        if file is None:
            file = sys.stdout
        file.write(message)
