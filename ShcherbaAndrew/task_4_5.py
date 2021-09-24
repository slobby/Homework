#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Callable, List
import csv


def remember_result(func: Callable) -> Callable:
    result = None
    def wrapper(*args,**kwargs):
        nonlocal result
        print(f"Last result = '{result}'")
        result = func(*args,**kwargs)
        return result
    return wrapper

@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result

if __name__ == "__main__":
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)
    
