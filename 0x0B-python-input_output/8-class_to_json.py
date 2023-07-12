#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    A function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    json_dict = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value
    return json_dict
