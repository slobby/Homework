#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint

def divisors() -> None:
    print("Enter a number:")
    while True:
        try:
            num: int = int(input(), 10)
            div_numbers: list(int) = []
            i = 1
            while (i * i <= num):
                if (num % i == 0):
                    div_numbers.append(i)
                    if (num / i != i):
                        div_numbers.append(int(num / i))
                i += 1
            div_numbers.sort()
            print(f"Divisors of {num}:")
            pprint.pp(div_numbers, indent=4, width=80)
            print("Enter a new number, or Ctr+C to exit:")
            
        except KeyboardInterrupt:
            print("Exit")
            break
        except Exception as ex:
            print(ex)
            print("Unhandled exception")
            break

if __name__ == "__main__":
    divisors()
