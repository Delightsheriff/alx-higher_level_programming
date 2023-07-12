#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """
    A function that returns the JSON representation of an object (string)
    """
    return json.loads(my_str)
