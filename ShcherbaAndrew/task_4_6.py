#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Callable, List
import csv


def call_once(func: Callable) -> Callable:
    is_called = False
    result = None
    def wrapper(*args,**kwargs):
        nonlocal is_called
        nonlocal result
        if is_called:
            return result
        else:
            result=func(*args,**kwargs)
            is_called=True
            return result
    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    
