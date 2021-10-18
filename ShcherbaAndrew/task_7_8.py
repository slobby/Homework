#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MySquareIterator:
    def __init__(self, it: list[int]):
        self.it = iter(it)

    def __iter__(self):
        return (i ** 2 for i in self.it)


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)
