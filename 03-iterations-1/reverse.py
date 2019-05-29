#!/usr/bin/env python3
"""
Takes a string as input and outputs the reverse
"""


def reverse_str(string_arg):
    new_string = list(string_arg)
    new_string.reverse()
    new_string = "".join(new_string)
    return new_string

print(reverse_str("bananas are the best"))