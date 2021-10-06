#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from string import ascii_lowercase, ascii_letters


class Cipher:
    def __init__(self, keyword: str) -> None:
        keyword_lower = keyword.lower()
        pure_keyword_lower = sorted(set(keyword_lower), key=keyword_lower.index)
        new_lower_alpabet = "".join(
            pure_keyword_lower
            + [l for l in ascii_lowercase if l not in pure_keyword_lower]
        )
        self.new_alpabet = new_lower_alpabet + new_lower_alpabet.upper()

    def encode(self, clause: str) -> str:
        return clause.translate(str.maketrans(ascii_letters, self.new_alpabet))

    def decode(self, clause: str) -> str:
        return clause.translate(str.maketrans(self.new_alpabet, ascii_letters))


if __name__ == "__main__":
    cipher = Cipher("crypto")
    print(cipher.encode("Hello world"))
    print(cipher.decode("Fjedhc dn atidsn"))
