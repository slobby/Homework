#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Dict, Tuple
from functools import reduce


def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    result = {}
    for d in args:
        for key, value in d.items():
            result[key] = result[key] + value if key in result else value
    return result


def main():
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))


if __name__ == "__main__":
    main()
