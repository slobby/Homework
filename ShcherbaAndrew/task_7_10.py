#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def endless_generator() -> int:
    start = 1
    while True:
        yield start
        start += 2


if __name__ == "__main__":
    gen = endless_generator()
    t = 0
    while t < 25:
        print(next(gen))
        t += 1
