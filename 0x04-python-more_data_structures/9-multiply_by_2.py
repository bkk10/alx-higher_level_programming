#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_mul = {}
    for key, value in a_dictionary.items():
        dic_mul[key] = value * 2
    return dic_mul
