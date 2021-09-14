#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint
from typing import Dict, List

def uniq_val(input_list: List[Dict[str, str]]) -> List[str]:
    interm_set: str = set()
    for item in input_list:
        if len(item) != 1:
            raise IndexError
        _, val =  item.popitem()
        interm_set.add(val)
    return interm_set

def handele_list(input_list: List[Dict[str, str]]) -> None:
    print("Input:")
    pprint.pp(il, indent=4)
    print("Output:")
    pprint.pp(uniq_val(il), indent=4)

if __name__ == "__main__":
    il = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
    handele_list(il)