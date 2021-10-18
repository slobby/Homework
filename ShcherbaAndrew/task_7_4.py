#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def supress(func):
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
        except:
            print("Supress errors")
        else:
            print("No errors")
        finally:
            return result

    return wrapper


@supress
def foo():
    raise ValueError()


@supress
def boo():
    pass


if __name__ == "__main__":
    foo()
    boo()
