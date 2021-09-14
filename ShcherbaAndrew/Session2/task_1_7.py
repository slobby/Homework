#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint
from typing import Tuple

def conv_tuple(input_tuple: Tuple[int, ...]) -> int:
    DEC: int = 10
    number: int = 0
    power: int = len(input_tuple)-1
    for k, v in enumerate(input_tuple):
        number += v * (DEC**power)
        power -=1
    return number

def handele_list(t) -> None:
    print("Input:")
    pprint.pp(t, indent=4)
    print("Output:")
    pprint.pp(conv_tuple(t), indent=4)

if __name__ == "__main__":
    t = (5,1,2,3,4)
    handele_list(t)
