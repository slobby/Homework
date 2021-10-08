#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Sun:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Sun, cls).__new__(cls)
        return cls._instance


if __name__ == "__main__":
    b = Sun()
    c = Sun()
    print(b is c)
