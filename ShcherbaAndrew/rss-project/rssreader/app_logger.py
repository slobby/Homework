# -*- coding: utf-8 -*-
"""Logging module."""


import logging
import sys
import os
from rssreader.constants import RSS_VERBOSE
from rssreader.constants import PROTOCOL_CSV

log_format: str = f"%(asctime)s - [%(levelname)s]:%(name)s - \
(%(filename)s:%(funcName)s:%(lineno)d) - %(message)s"


def get_file_handler(filename: str) -> logging.Handler:
    """Create file handler.

    Args:
        filename (str): log file name

    Returns:
        logging.Handler: file handler for logger
    """
    file_handler = logging.FileHandler(filename, encoding="utf8", delay=True)
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(log_format))
    return file_handler


def get_stream_handler() -> logging.Handler:
    """Create console handler.

    Returns:
        logging.Handler: console handler for logger
    """
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(log_format))
    return stream_handler


def get_logger(name: str, filename: str = PROTOCOL_CSV) -> logging.Logger:
    """Create logger.

    Args:
        name (str): logger name
        filename (str): log file name

    Returns:
        logging.Logger: logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler(filename))
    if os.environ.get(RSS_VERBOSE, "FALSE") == "TRUE":
        logger.addHandler(get_stream_handler())
    logger.propagate = False
    return logger
