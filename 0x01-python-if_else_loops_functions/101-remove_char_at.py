#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) - 1 or n < 0:
        return str
    str = str.replace(str[n],"")
    return str
