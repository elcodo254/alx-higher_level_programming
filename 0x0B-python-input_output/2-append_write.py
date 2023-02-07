#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file(UTF8)

    Args:
        filename (str): Name of file
        text (str): string o be appended
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
