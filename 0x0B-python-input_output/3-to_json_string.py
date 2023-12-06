#!/usr/bin/python3
import json

""" This module reutrns the JSON representation of an object """


def to_json_string(my_obj):
    """
        This function handles JSON files

        Args:
            my_obj (obj): object variable

        Returns:
            The JSON representation of an object string
    """

    return json.dumps(my_obj)
