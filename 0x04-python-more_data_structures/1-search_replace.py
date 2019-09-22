#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if o == search else o for o in my_list]
