#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Dict
from collections import OrderedDict

def sort_dict(input: Dict) -> Dict:
    key_list: List = sorted(input)
    for key in key_list:
        input[key] = input.pop(key)
    return input
   
if __name__ == "__main__":
    temp = {"e":7,"f":3,"d":56,"c":9,"b":1,"a":8}
    print(temp)
    print(sort_dict(temp))