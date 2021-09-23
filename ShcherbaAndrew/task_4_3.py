#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
import csv


def get_top_performers(file_path, number_of_top_students=5) -> List[str]:
    try:
        with open(file_path, encoding="utf-8", newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            return [item["student name"] for item in sorted(reader, key=lambda line: line["average mark"], reverse=True)[:number_of_top_students]]
    except:
        print('An exception occurred')
        return []

    
def write_top_olders(file_path) -> None:
    try:
        with open(file_path, encoding="utf-8", newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            with open("new.csv", "w",  encoding="utf-8",  newline="") as fw:
                writer = csv.DictWriter(fw, fieldnames=reader.fieldnames, delimiter=',')
                writer.writeheader()
                writer.writerows(sorted(reader, key=lambda line: line["age"], reverse=True))
    except:
        print('An exception occurred')


if __name__ == "__main__":
    input_file_path = "../data/students.csv"
    # print(get_top_performers(input_file_path))
    write_top_olders(input_file_path)
    
