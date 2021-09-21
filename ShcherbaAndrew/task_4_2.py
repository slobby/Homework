#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_palindrome(input: str) -> bool:
    raw_string ="".join(item for item in str(input.lower()) if item.isalnum())
    return raw_string == raw_string[::-1]


def main():
    print("Enter a string:")
    while True:
        try:
            input_string: str = input()
            print(is_palindrome(input_string))
            print("Enter a new string, or Ctr+C to exit:")
        except KeyboardInterrupt:
            print("Exit")
            break
        except:
            print("Unhandled exception")
            break

if __name__ == "__main__":
    main()