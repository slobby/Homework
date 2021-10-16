# -*- coding: utf-8 -*-
"""date_type module."""

import time
from typing import Union
from app_logger import get_logger

logger = get_logger(__name__)


def date_type(value: str, format: str) -> Union[time.struct_time, None]:
    date_time = None
    """Try convert string to time.struct_time type.

    Args:
        value (str): input value

    Returns:
        time.struct_time: output value
    """
    try:
        date_time = time.strptime(value, format)
    except ValueError:
        logger.error(f"Couldn`t convert [value] in datetime, with format [{format}]")
    return date_time
