#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Tuple


def get_digits(num: int) -> Tuple[int]:
    return tuple(list(str(num)))


def main():
    print(get_digits(87178291199))
    print(get_digits(42))


if __name__ == "__main__":
    main()
