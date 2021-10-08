#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Union


class Money:
    _ex_rate = {"USD": 1, "EUR": 0.93, "BYN": 2.6, "RUB": 80, "JPY": 0.009, "CH": 44.0}

    def convert(self, other: Money) -> Union[float, int]:
        return (
            other._amount
            * self._ex_rate[self._currency]
            / self._ex_rate[other._currency]
        )

    def __init__(self, amount: Union[float, int], currency: str = "USD") -> None:
        if currency not in self._ex_rate:
            raise TypeError("Param currency is invalid!")
        self._amount = amount
        self._currency = currency

    def __str__(self) -> str:
        return f"{self._amount:.2f} {self._currency}"

    def __add__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Param is not Money!")
        return Money(self._amount + self.convert(other), self._currency)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                other = Money(0)
        if not isinstance(other, Money):
            raise TypeError("Param is not Money!")
        return self.__add__(other)

    # __iadd__ = __add__

    def __sub__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Param is not Money!")
        return Money(self._amount - self.convert(other), self._currency)

    def __mul__(self, val):
        if not isinstance(val, (float, int)):
            raise TypeError("Param is not valid!")
        return Money(self._amount * val, self._currency)

    __rmul__ = __mul__

    def __div__(self, val):
        if not isinstance(val, (float, int)):
            raise TypeError("Param is not valid!")
        return Money(self._amount / val, self._currency)

    __truediv__ = __div__

    def __lt__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Param is not Money!")
        return self._amount < other._amount

    def __gt__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Param is not Money!")
        return self._amount > other._amount

    def __le__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Param is not Money!")
        return self._amount <= other._amount

    def __ge__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Param is not Money!")
        return self._amount >= other._amount

    def __eq__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Param is not Money!")
        return self._amount == self.convert(other)

    def __ne__(self, other):
        return not self.__eq__()


if __name__ == "__main__":
    x = Money(10, "BYN")
    y = Money(11)  # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")
    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)
