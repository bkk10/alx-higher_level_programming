#!/usr/bin/python3
"""
module that checks whether object inherited directly/indirectly from a class
"""
def inherits_from(obj, a_class):
    """return true if inherited directly/indirectly from class otherwise fals"""
    return isinstance(obj, a_class) and type(obj) is not a_class
