#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Iterable


class MyNumberCollection:
    def __init__(self, *args) -> None:
        if len(args) == 1 and isinstance(args[0], Iterable):
            for item in args[0]:
                if not isinstance(item, int):
                    raise TypeError("MyNumberCollection supports only numbers!")
            self.items = list(args[0])
        else:
            start, stop, step = args
            if (
                isinstance(start, int)
                and isinstance(stop, int)
                and isinstance(step, (int, None))
            ):
                step = step or 1
                self.items = [item for item in range(start, stop, step)]

    def __iter__(self):
        return iter(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} - object is not a number!")
        self.items.append(value)

    def __add__(self, other):
        if not isinstance(other, MyNumberCollection):
            raise TypeError(f"{other} - object is not a MyNumberCollection!")
        result = self.items + other.items
        return MyNumberCollection(result)

    def __getitem__(self, index):
        return self.items[index] ** 2


if __name__ == "__main__":
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
    # col3 = MyNumberCollection((1, 2, 3, "4", 5))
    col1.append(7)
    print(col1)
    # col2.append("string")
    print(col1 + col2)
    print(col1)
    print(col2)
    print(col2[4])
    for item in col1:
        print(item)
