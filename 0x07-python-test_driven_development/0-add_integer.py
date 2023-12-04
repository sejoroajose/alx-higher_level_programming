#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers together and returns the value
    
    Args:
        a (int): first input integer
        b (int): second input integer

    Returns:
        int: The addition of the two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
