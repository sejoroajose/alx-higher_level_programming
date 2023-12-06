#!/usr/bin/python3

""" This module writes a string to a text file """


def write_file(filename="", text=""):

    """
        The function is used to write a string into a text file

        Args:
            filename (str): The name of the text file to read
            text (str): The  place it will write the text

        Returns:
            The number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as file:
        chars = file.write(text)
        return chars
