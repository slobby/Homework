# -*- coding: utf-8 -*-
"""Test rss reader functions."""


import sys
import pytest
from rssreader.rss_reader import main


def test_rss_reader_exit_code(get_feed_list):
    sys.argv = ["test"]
    with pytest.raises(SystemExit) as e:
        main()
    assert e.type == SystemExit
    assert e.value.code == 1
