#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import pprint

def chr_freq() -> None:
    print("Enter a string:")
    while True:
        try:
            input_string: str = input()
            freq: dict[str, int] = { k: len(list(g)) for k, g in itertools.groupby(sorted(input_string.lower()))}
            print("Unique key-value:")
            pprint.pp(freq, indent=4, width=1)
            print("Enter a new string, or Ctr+C to exit:")
        except KeyboardInterrupt:
            print("Exit")
            break
        except Exception as ex:
            print(ex)
            print("Unhandled exception")
            break

if __name__ == "__main__":
    chr_freq()
