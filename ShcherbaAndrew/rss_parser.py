# -*- coding: utf-8 -*-
"""Main module."""

import sys
from command_line_parser import get_args

params = get_args()

from app_logger import get_logger
from get_feeds import get_feeds
from utils import print_to_output


logger = get_logger(__name__)
# print(params.__dict__)

try:
    feeds = get_feeds(params)
    print_to_output(feeds, params)
except Exception as ex:
    if hasattr(ex, "message"):
        print(ex.message)
    else:
        logger.error("Error. Unrecognized error has occured", exc_info=1)
        print("Error. Unrecognized error has occured. See log or use --verbose mode")
    sys.exit(1)
