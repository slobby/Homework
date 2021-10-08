#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from typing import List, Union


class Pagination:
    def __init__(self, text: str, symbols_per_page: int = None) -> None:
        if symbols_per_page is None:
            raise IndexError("Invalid index. Symbols_per_page is missing!")
        if symbols_per_page <= 0:
            raise IndexError(
                "Invalid index. Symbols_per_page index must be more than 0!"
            )
        self._text = text
        self._symbols_per_page = symbols_per_page
        self._item_count = len(self._text)
        self._page_count = self._item_count // self._symbols_per_page + (
            self._item_count % self._symbols_per_page > 0
        )

    @property
    def item_count(self) -> int:
        return self._item_count

    @property
    def page_count(self) -> int:
        return self._page_count

    def count_items_on_page(self, page: int = None) -> int:
        if page is None:
            raise IndexError("Invalid index. Page is missing!")
        if page >= 0 and page < self._page_count:
            if (
                page + 1 == self._page_count
                and self._item_count % self._symbols_per_page > 0
            ):
                return self._item_count % self._symbols_per_page
            else:
                return self._symbols_per_page
        raise IndexError("Invalid index. Page out of range!")

    def display_page(self, page: int = None) -> str:
        if page is None:
            raise IndexError("Invalid index. Page is missing!")
        if page >= 0 and page < self._page_count:
            start = page * self._symbols_per_page
            stop = (page + 1) * self._symbols_per_page
            return self._text[start:stop]
        raise IndexError("Invalid index. Page out of range!")

    def find_page(self, pattern: str) -> List[int]:
        result: List[int] = []
        for match in re.finditer(pattern, self._text):
            first_in = match.start() // self._symbols_per_page
            last_in = match.end() // self._symbols_per_page
            result.extend(range(first_in, last_in + 1))
        if not result:
            raise Exception(f"'{pattern}' is missing on the pages")
        return result


if __name__ == "__main__":
    pages = Pagination("Your beautiful text!", 5)
    print(pages.page_count)
    print(pages.item_count)
    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(3))
    # print(pages.count_items_on_page(4))
    print(pages.find_page("Your"))
    print(pages.find_page("e"))
    print(pages.find_page("beautiful"))
    print(pages.find_page("great"))
