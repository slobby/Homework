#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class OutOfRangeError(Exception):
    def __str__(self):
        return "Maximal value is reached"


class Counter:
    def __init__(self, start: int = 0, stop: int = None) -> None:
        self._start = start
        self._stop = stop

    def increment(self):
        try:
            if self._stop and self._start == self._stop:
                raise OutOfRangeError
            self._start += 1
        except OutOfRangeError as ex:
            print(ex)

    def get(self):
        print(self._start)


if __name__ == "__main__":
    c = Counter(start=42)
    c.increment()
    c.get()

    c = Counter()
    c.increment()
    c.get()
    c.increment()
    c.get()

    c = Counter(start=42, stop=43)
    c.increment()
    c.get()
    c.increment()
    c.get()
