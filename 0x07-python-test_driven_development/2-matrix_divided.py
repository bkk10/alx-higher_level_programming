#!/usr/bin/python3
"""
This function divides all elements of a matrix by a given number.
"""

def matrix_divided(matrix, div):
    # Check if matrix is a list of lists of numbers (int or float)
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all elements inside the rows are numbers (int or float)
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that all rows are the same length
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Cannot divide by 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with each element divided and rounded to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
