#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from task_7_5 import NotEven, IsNotGreaterThanTwo, is_even


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def goldbach(number):
    try:
        number = int(number)
        if not isinstance(number, int):
            raise ValueError
        is_even(number)
        for x in range(2, int(number / 2) + 1):
            if isPrime(x):
                y = number - x
                if isPrime(y):
                    return f"x={x}, y={y}"
        return f"Coudn`t found Primes for {number}"
    except NotEven:
        return f"Error! {number} is not an even number"
    except IsNotGreaterThanTwo:
        return f"Error {number} is not greater than 2, Goldbach Conjecture is observed only in even numbers greater than 2"
    except ValueError:
        return f"Error! {no} is not an number"


def main():
    while True:
        no = input("Enter Even Number greater than 2 or 'q' for exit:")
        if no == "q":
            break
        print(goldbach(int(no)))


if __name__ == "__main__":
    main()
