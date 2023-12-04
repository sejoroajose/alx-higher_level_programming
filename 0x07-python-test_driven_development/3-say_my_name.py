#!/usr/bin/python3

"""
This module prints the name of an individual
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the name of an individual

    Args:
        first_name (str): first name of the individual
        last_name (str): Last name of the individual

    Returns:
        str: Formatted sentence carrying the name of the individual

    Raises:
        TypeError: If the arguments aren't strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    return("My name is %s %s", first_name, last_name)
