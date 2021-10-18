#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from contextlib import ContextDecorator


class ExecutionTimeManager(ContextDecorator):
    def __init__(self, filename: str):
        self._filename = filename
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        with open(self._filename, mode="a") as f:
            f.write(f"Delta={time.time()-self.start_time}\n")
        if exc_type:
            return True


@ExecutionTimeManager("log.csv")
def foo():
    time.sleep(1.26)


if __name__ == "__main__":
    fm = ExecutionTimeManager("log.csv")
    with fm:
        time.sleep(0.025)

foo()
