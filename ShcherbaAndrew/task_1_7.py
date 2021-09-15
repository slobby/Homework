#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint
from typing import Tuple
import functools

def conv_tuple(input_tuple: Tuple[int, ...]) -> int:
    DEC: int = 10
    return functools.reduce(
        lambda sum, item : sum + item[1] * (DEC**item[0]),
        enumerate(reversed(input_tuple)),
                  0)

def handele_list(t) -> None:
    print("Input:")
    pprint.pp(t, indent=4)
    print("Output:")
    pprint.pp(conv_tuple(t), indent=4)

if __name__ == "__main__":
    t = (5,1,2,3,4)
    handele_list(t)
