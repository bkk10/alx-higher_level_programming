#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_product = sum(score * weight for score, weight in my_list)

    # Calculate the sum of weights
    total_weight = sum(weight for _, weight in my_list)

    # Calculate the weighted average
    weighted_average = total_product / total_weight

    return weighted_average
