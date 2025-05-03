#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = []
    total = 0
    for num in my_list:
        if (num not in  result):
            result.append(num)
            total += num
    return total
