# -*- coding: utf-8 -*-
"""COnstats module."""

# application
import re


VERSION = "1.1"
TIMEOUT = 5
TAG_RE = re.compile(r"<[^>]+>")

ENCODING_IN = "utf-8"
ENCODING_OUT = "utf-8"

# log file
PROTOCOL_CSV = "protocol.csv"

# enviroments
RSS_VERBOSE = "RSS_VERBOSE"


NO = "Нет"
ERROR_CELL = "ERROR_CELL"
MERGED = "MERGED"
EMPTY = ""

IS_FILLED = True
TABLE1_COL_NUM = 10
TABLE2_COL_NUM = 4
TABLE4_COL_NUM = 23
TABLE10_COL_NUM = 5
