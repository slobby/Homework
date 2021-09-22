#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Set
from functools import reduce
import string


def test_1_1(*strings: str) -> Set[str]:
    return reduce(lambda acc, s: acc & s,
                  map(lambda x: set(x), strings))


def test_1_2(*strings: str) -> Set[str]:
    return reduce(lambda acc, s: acc | s,
                  map(lambda x: set(x), strings))


def test_1_3(*strings: str) -> Set[str]:
    acc = set()
    list_set = list(map(lambda x: set(x), strings))
    for _ in range(len(list_set)-1):
        s = list_set.pop()
        for item in list_set:
            acc = acc | s & item
    return acc


def test_1_4(*strings: str) -> Set[str]:
    return reduce(lambda acc, s: acc - s,
                  map(lambda x: set(x.lower()), strings),
                  set(string.ascii_lowercase),
                  )


def main():
    test_strings = ["hello", "world", "python", ]
    print(test_1_1(*test_strings))
    print(test_1_2(*test_strings))
    print(test_1_3(*test_strings))
    print(test_1_4(*test_strings))


if __name__ == "__main__":
    main()
