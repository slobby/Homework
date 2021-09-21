#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def split_str(input: str, sep=None, maxsplit=-1) -> List[str]:
    inner_sep: str = sep if sep else " "
    sep_len = len(inner_sep)
    result: List[str] = []
    start_index = 0
    if maxsplit < 0:
        while start_index < len(input):
            index = input.find(inner_sep, start_index)
            if index != -1:
                result.append(input[start_index:index])
                start_index = index + sep_len
            else:
                result.append(input[start_index:])
                break
    else:
        while start_index < len(input):
            if maxsplit > 0:
                index = input.find(inner_sep, start_index)
                if index != -1:
                    result.append(input[start_index:index])
                    start_index = index + sep_len
                else:
                    result.append(input[start_index:])
                    break
                maxsplit -= 1
            else:
                result.append(input[start_index:])
                break
    return result


def main():
    print(split_str("fdgs ,,dsffff", sep=','))


if __name__ == "__main__":
    main()
