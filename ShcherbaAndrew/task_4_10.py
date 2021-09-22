#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Dict


def generate_squares(num: int) -> Dict[int, int]:
    return {i: i**2 for i in range(1, num+1)}


def main():
    print(generate_squares(5))


if __name__ == "__main__":
    main()
