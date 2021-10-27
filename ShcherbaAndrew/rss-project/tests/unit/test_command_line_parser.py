# -*- coding: utf-8 -*-
"""Test command line functions."""


import os
import sys
import time
import pytest
from pytest_mock import MockerFixture
from rssreader.command_line_parser import check_path, get_args
from rssreader.interfaces import ProgramArgs


def test_check_ext_path(mocker: MockerFixture):
    excpect_ext = "ext"
    test_path = "test_file." + excpect_ext
    assert check_path(excpect_ext, test_path) == os.path.abspath(test_path)


def test_check_error_path():
    with pytest.raises(ValueError) as e_info:
        excpect_ext = "ext"
        unexpect_ext = "err"
        test_path = "test_file." + unexpect_ext
        check_path(excpect_ext, test_path)


def test_get_args_wrong_lim():
    with pytest.raises(SystemExit) as e:
        sys.argv = ["test", "dfdsgfdg", "--limit", "-6"]
        get_args()
    assert e.type == SystemExit
    assert e.value.code == 1


def test_get_args_missed_source():
    with pytest.raises(SystemExit) as e:
        sys.argv = ["test", "--limit", "66"]
        get_args()
    assert e.type == SystemExit
    assert e.value.code == 1


def test_get_args():
    args_list = ["test",
                 "url://fake",
                 "--json",
                 "--verbose",
                 "--limit",
                 "5",
                 "--date",
                 "20211021",
                 "--to-html",
                 "default.html",
                 "--to-fb2",
                 "default.fb2"]
    sys.argv = args_list
    args = get_args()
    assert type(args) == ProgramArgs
    assert args.source == args_list[1]
    assert args.is_json == True
    assert args.is_verbose == True
    assert args.limit == 5
    assert args.date == time.strptime("20211021", "%Y%m%d")
    assert args.to_html == os.path.abspath("default.html")
    assert args.to_fb2 == os.path.abspath("default.fb2")
