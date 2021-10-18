#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ErrorEven(ValueError):
    pass


class NotEven(ErrorEven):
    pass


class IsNotGreaterThanTwo(ErrorEven):
    pass


def is_even(number: int) -> bool:
    if number <= 2:
        raise IsNotGreaterThanTwo
    if number % 2 != 0:
        raise NotEven
    return True


if __name__ == "__main__":
    is_even(6)
    is_even(2)
    is_even(1)
