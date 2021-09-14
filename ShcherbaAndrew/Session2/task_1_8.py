#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Tuple, List

def mult_table(first_range: Tuple[int, int], second_range: Tuple[int, int]) -> List[List[int]]:
    out_list = list()
    for i in range(first_range[0], first_range[1]+1):
        row = list()
        for j in range(second_range[0], second_range[1]+1):
            row.append(i * j)
        out_list.append(row)
    return out_list
            
def pretty_print_row(row: List[str], underscore = False, cell_width = None) -> None:
    cell_width = cell_width if cell_width else len(max(row))
    for item in row:
        print(f" {item: ^{cell_width}} |", end = '')
    print()
    if underscore:
        print(f"{'-'*len(row)*(cell_width + 3)}")

def pretty_print_mult_table(first_range: Tuple[int, int], second_range: Tuple[int, int]) -> None:
    mult = mult_table(first_range, second_range)
    cell_width = len(str(mult[-1][-1]))
    head: List[str] = list("\\")
    head.extend(map(lambda item : str(item), range(second_range[0], second_range[1] + 1)))
    pretty_print_row(head, True, cell_width)
    for i, row in enumerate(mult):
        row.insert(0, first_range[0] + i)
        pretty_print_row(map(lambda item : str(item), row), cell_width = cell_width)

def handler() -> None:
    try:
        print("Enter a:")
        a : int = int(input())
        print("Enter b:")
        b : int = int(input())
        print("Enter c:")
        c : int = int(input())
        print("Enter d:")
        d : int = int(input())       
        pretty_print_mult_table((a,b), (c,d))
    except Exception as ex:
        print(ex)
        print("Unhandled exception")

if __name__ == "__main__":
    handler()