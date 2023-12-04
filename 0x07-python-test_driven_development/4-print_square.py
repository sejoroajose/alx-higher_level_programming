#!/usr/bin/python3

"""
This module prints a squrare with the charachter #
"""
def print_square(size):

    """
    Prints a square with the character

    Args:
        size (int): the number of times the character will form the length and breath

    Returns: A square of lengths (size)

    Raises:
        TypeError: If the type is not an integer
        ValueError:  If  size is less than 0

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float:
        raise TypeError("size must be an integer")

    grid = [("#" for i in range(size)) for j in range(size)]
    for row in grid:
        print("".join(row))
