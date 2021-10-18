#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup module."""

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name="rssreader",
    version="1.0",
    author="Andrew Shcherba",
    packages=find_packages(include=["rssreader", "rssreader.*"]),
    long_description=open(join(dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4==4.10.0",
        "jsonpickle==2.0.0",
        "lxml==4.6.3",
        "requests==2.26.0",
    ],
    entry_points={"console_scripts": ["rss_reader=rssreader.rss_reader:main"]},
)
