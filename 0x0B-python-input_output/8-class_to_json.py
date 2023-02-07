#!/usr/bin/python3
""" Define a class-to-json function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

    Args:
        obj (object): an instance of a class
    Returns:
        dict: dictionary description 
    """
    return obj.__dict__
