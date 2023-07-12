#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file”
    """
    with open(filename, 'r') as temp:
        return json.loads(temp.read())