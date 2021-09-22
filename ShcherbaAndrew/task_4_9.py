#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Tuple, Any, Union
from functools import reduce


def get_pairs(lst: List[Any]) -> Union[List[Tuple[Any]], None ]:
    if len(lst) < 2:
        return None    
    next(help_iter := iter(lst))
    return list(zip(iter(lst), help_iter))


def main():
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))


if __name__ == "__main__":
    main()
