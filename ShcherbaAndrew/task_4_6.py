#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def get_longest_word(s: str) -> str:
    lines: List[str] = s.splitlines()
    words: List[str] = []
    for line in lines:
        words.extend(line.split())
    print(words)
    words.sort(key=len, reverse=True)
    return words[0]


def main():
    print(get_longest_word('Python is simple and effective!'))
    print(get_longest_word('Any pythonista like namespaces a lot.'))


if __name__ == "__main__":
    main()
