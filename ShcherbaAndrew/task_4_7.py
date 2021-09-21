#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from functools import reduce


def foo(input: List[int]) -> List[int]:
    mult = reduce(lambda x, y: x*y, input, 1)
    return [int(mult/number) for number in input]


def main():
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))


if __name__ == "__main__":
    main()
