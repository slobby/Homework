#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import pprint

def sort_txt() -> None:
    input_file_path = "../data/unsorted_names.txt"
    output_file_path = "../data/sorted_names.txt"
    try:
      with open(input_file_path, encoding='utf-8') as fr:
          lines = fr.readlines()
          lines.sort()
          with open(output_file_path, 'w', encoding='utf-8') as fw:
              fw.writelines(lines)
    except Exception as ex:
        print(ex)
        print('An exception occurred')


if __name__ == "__main__":
    sort_txt()