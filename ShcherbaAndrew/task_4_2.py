#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Dict


def most_common_words(filepath, number_of_words=3) -> None:
    temp_words: Dict[str, int] = {}
    try:
        with open(filepath, encoding='utf-8', newline=None) as fr:
            for line in fr:
                words_list = filter(lambda x: len(x) != 0,
                                    map(lambda w: w.lower().strip("\r\n .,"),
                                    line.split(" ")))
                for word in words_list:
                    temp_words[word] = temp_words[word] + \
                        1 if word in temp_words else 1
        sorted_words = list(map(lambda item: item[0], sorted(
            temp_words.items(), key=lambda item: item[1], reverse=True)))
        print(sorted_words[:number_of_words])
    except:
        print('An exception occurred')


if __name__ == "__main__":
    input_file_path = "../data/lorem_ipsum.txt"
    most_common_words(input_file_path, number_of_words=3)
