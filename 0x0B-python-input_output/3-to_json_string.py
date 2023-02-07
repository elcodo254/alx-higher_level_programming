#!/usr/bin/python3
"""Defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation object(string)."""
    return json.dumps(my_obj)