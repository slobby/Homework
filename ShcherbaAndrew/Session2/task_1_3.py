#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint

def uniq_word() -> None:
    print("Enter comma sepatated sequence of words:")
    while True:
        try:
            input_string: str = input()
            words: list[int] = sorted(set(map(lambda arg : arg.strip(), input_string.lower().split(","))))
            print("Unique words:")
            pprint.pp(words, indent=4, width=1)
            print("Enter a new sequence of words, or Ctr+C to exit:")
        except KeyboardInterrupt:
            print("Exit")
            break
        except Exception as ex:
            print(ex)
            print("Unhandled exception")
            break

if __name__ == "__main__":
    uniq_word()
