#!/bin/usr/python3
def append_after(filename="", search_string="", new_string=""):

    with open(filename, 'r') as f:
        buf = f.readlines()

    with open(filename, 'w') as w:
        for line in buf:
            if line == search_string:
                line += new_string
            w.write(line)
