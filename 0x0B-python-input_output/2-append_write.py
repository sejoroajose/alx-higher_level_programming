#!/usr/bin/python3

""" This module appends a string to  a text file """


def append_write(filename="", text=""):

    """
        This function is used to append a string to a text file

        Args:
            filename (str): name of destination file
            text (str): string to append

        Returns:
             The number of string appended
    """

    with open(filename, 'a', encoding='utf-8') as file:
        chars_added = file.write(text)
        return chars_added
