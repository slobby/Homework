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

# DB
DB_FILE = "db/db.pickle"

