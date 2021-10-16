# -*- coding: utf-8 -*-
"""
МОдуль констант

"""
# application
import re


VERSION = "1.1"
TIMEOUT = 5
TAG_RE = re.compile(r"<[^>]+>")

ENCODING_IN = "utf-8"
ENCODING_OUT = "utf-8"

FILE_SIGNALS_CSV = "signals.csv"
FILE_SWITCHES_CSV = "switches.csv"
FILE_SECTIONS_CSV = "sections.csv"
FILE_UNCONTROLLED_SECTIONS_CSV = "uncontrolled_sections.csv"
FILE_SWITCH_SECTIONS_CSV = "switch_sections.csv"
FILE_TRACKS_CSV = "tracks.csv"
FILE_PATHS_CSV = "paths.csv"
FILE_ROUTERS_CSV = "routes.csv"
PROTOCOL_CSV = "protocol.csv"

# List of files
FILE_LIST = [
    FILE_SIGNALS_CSV,
    FILE_SWITCHES_CSV,
    FILE_SECTIONS_CSV,
    FILE_UNCONTROLLED_SECTIONS_CSV,
    FILE_SWITCH_SECTIONS_CSV,
    FILE_TRACKS_CSV,
    FILE_PATHS_CSV,
    FILE_ROUTERS_CSV,
]

CSV_DELIMITER = ";"
CSV_ROW_VECTOR_LENGTH = 1
CSV_ROW_SWITCH_SECTIONS_LENGTH = 2
CSV_ROW_ROUTE_LENGTH = 10

START_BRACKET = "["
END_BRACKET = "]"
SEP = ","
TRIM_CHAR = " "
CROSS_CHARS = "01"

SOURSE_TABLE_DIR = "templatetables"
OUTPUT_DIR = "dist"

# log file
LOG_FILE = "protocol.csv"

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
