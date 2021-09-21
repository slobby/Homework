#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def replace_char(input: str) -> str:
    """[Replace ' char to " and vice versa in given 'input']

    Args:
        input (str): [original string]

    Returns:
        str: [new string]
    """
    
    def pinch(input: str) -> str:
        SINGLE_QUOTE = r"'"
        DOUBLE_QUOTE = r'"'
        if input == SINGLE_QUOTE:
            return DOUBLE_QUOTE
        elif input == DOUBLE_QUOTE:
            return SINGLE_QUOTE
        return input
    
    return "".join(pinch(item) for item in list(input))


def main():
    print("Enter a string:")
    while True:
        try:
            input_string: str = input()
            print(replace_char(input_string))
            print("Enter a new string, or Ctr+C to exit:")
        except KeyboardInterrupt:
            print("Exit")
            break
        except:
            print("Unhandled exception")
            break

if __name__ == "__main__":
    main()