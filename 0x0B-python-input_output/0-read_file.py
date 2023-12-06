#!/usr/bin/python3

"""This module reads a text file"""


def read_file(filename=""):

    """"

        The function is used to read a file and print it to the stdout

        Args:
            filename (str): name of the file to be read

        Returns:
            The content of the specified text file.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()

    print(read_data, end='')
