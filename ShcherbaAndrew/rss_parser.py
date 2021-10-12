# -*- coding: utf-8 -*-
"""Main module."""

from app_logger import get_logger
from command_line_parser import get_args

params = get_args()
logger = get_logger(__name__)
logger.info("info massage")
logger.warning("warning massage")
print(vars(params))
