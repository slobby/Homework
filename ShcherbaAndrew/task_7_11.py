#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def endless_fib_generator() -> int:
    a, b = 0, 1
    while True:
        yield b
        a, b = b, b + a


if __name__ == "__main__":
    gen = endless_fib_generator()
    t = 0
    while t < 25:
        print(next(gen))
        t += 1
