#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    result: List[str] = []
    s_len = len(s)
    indexes = [item for item in indexes if (item > 0 and item < s_len)]
    helper_indexes = [0, *indexes]
    indexes.append(s_len)
    for srat, stop in zip(helper_indexes, indexes):
        result.append(s[srat:stop])
    return result


def main():
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    print(split_by_index("no luck", [42]))


if __name__ == "__main__":
    main()
