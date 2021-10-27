# -*- coding: utf-8 -*-
"""Test db service functions."""


from rssreader.interfaces import DBService


def test_db_create(get_feed_list):
    bd = DBService("test_db.pikle")
    bd.insert(get_feed_list)
    bd.find_all()
    assert len(bd.find_all()) == len(get_feed_list)
