#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def str_len() -> None:
    print("Enter a string:")
    while True:
        try:
            input_string: str = input()
            # print(input_string.__len__())
            count: int = 0
            for _ in input_string:
                count +=1
            print(f"length:{count}")
            print("Enter a new string, or Ctr+C to exit:")
        except KeyboardInterrupt:
            print("Exit")
            break
        except :
            print("Unhandled exception")
            break

if __name__ == "__main__":
    str_len()