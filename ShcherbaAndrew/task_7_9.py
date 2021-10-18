#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class EvenRange:
    def __init__(self, start=0, stop=0):
        self.start = (start + 1) if start % 2 != 0 else start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            result = self.start
            self.start += 2
            return result
        print("Out of numbers!")
        raise StopIteration


if __name__ == "__main__":
    # er1 = EvenRange(7, 11)
    # print(next(er1))
    # print(next(er1))
    # print(next(er1))

    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)
