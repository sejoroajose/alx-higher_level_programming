#!/usr/bin/python3

"""
This module is composed of a function that divides all elements of a matrix by a given integer
"""

def matrix_divided(matrix, div):
    """
    Divides all element of a matrix by an integr

    Args:
        matrix (list): list of matrix element
        div (int): integer used to divide matrix

    Returns:
        list: The list of the divided matrix elements

    Raises:
        TypeError: If the elements are not an int or a float
        TypeError: If Matrix is not the same size
        ZeroDivisionError: If the matrix is divided by zero

    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row of the matrix has same size
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")


    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix
