#!/usr/bin/python3
"""
create an inheritance class
"""
class MyList(list):
    """mylist is subclass of list"""
    def print_sorted(self):
        """that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
