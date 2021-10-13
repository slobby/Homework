# -*- coding: utf-8 -*-
"""date_type module."""

import time


def date_type(value: str) -> time.struct_time:
    """Try convert string to time.struct_time type.

    Args:
        value (str): input value

    Returns:
        time.struct_time: output value
    """
    return time.strptime(value, "%Y%m%d")
