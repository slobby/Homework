#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import sys


@contextmanager
def file_manager(filename, mode="r", encoding="utf-8"):
    f = None
    try:
        f = open(filename, mode=mode, encoding=encoding)
        yield f
    except:
        print(sys.exc_info())
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    fm = file_manager("test.csv")
    with fm as f:
        print(f.readline())
        f.write("Blabla")

    print("Continue here")
