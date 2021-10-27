# -*- coding: utf-8 -*-
"""Test utils functions."""


import argparse
import io
import time
from typing import List
import pytest
from pytest_mock import MockerFixture
from rssreader.interfaces import ProgramArgs
from rssreader.utils import date_type, trunc_feed_list, print_message, print_to_output
from pytest_mock import MockerFixture
from rssreader.errors import ZeroLimitAmountException


def test_date_type_return_None():
    date_string = "2010-05-10"
    date_format = "%Y%m%d"
    assert date_type(date_string, date_format) == None


def test_date_type_return_time_struct_time():
    date_string = "20100510"
    date_format = "%Y%m%d"
    result = date_type(date_string, date_format)
    assert type(result) == time.struct_time
    assert result == time.strptime(date_string, date_format)


def test_trunc_feed_list_return_empty_feeds_list():
    init_list = []
    handled_list = trunc_feed_list(init_list, 3)
    assert type(handled_list) == type([])
    assert len(handled_list) == 0


def test_trunc_feed_list_return_feeds_list(get_feed_list):
    init_list = get_feed_list
    handled_list = trunc_feed_list(init_list, 2)
    assert type(handled_list) == type([])
    assert len(handled_list) == 1


def test_print_message(mocker: MockerFixture):
    mock_out = mocker.patch('sys.stdout', new_callable=io.StringIO)
    test_message = "test_message"
    print_message(test_message)
    assert mock_out.getvalue() == test_message


# def test_in(mocker):
#     mocker.patch('builtins.input', side_effect=['the input you want to test'])

def test_print_to_output_raises_ZeroLimitAmountException():
    arg_namespace = argparse.Namespace()
    arg_namespace.__setattr__("limit", 0)
    args = ProgramArgs(arg_namespace)
    with pytest.raises(ZeroLimitAmountException) as e:
        print_to_output([], args)


# def test_print_to_output_call_to_string(mocker):
#     to_string = mocker.patch(
#         'rssreader.utils.feeds_to_string.feeds_to_string')
#     to_json = mocker.patch(
#         'rssreader.utils.feeds_to_json.feeds_to_json')

#     arg_namespace = argparse.Namespace()
#     arg_namespace.__setattr__("limit", 5)
#     arg_namespace.__setattr__("is_json", False)
#     args = ProgramArgs(arg_namespace)
#     feeds = []
#     print_to_output(feeds, args)
#     assert to_string.assert_called_once_with(feeds)
#     assert to_json.assert_not_called()
