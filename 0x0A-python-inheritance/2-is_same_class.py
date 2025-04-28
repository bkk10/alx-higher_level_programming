#!/usr/bin/python3
"""
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
"""
def is_same_class(obj, a_class):
    """return true if object is an instance os the specified class"""
    return type(obj) == a_class
