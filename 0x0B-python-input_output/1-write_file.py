#!/usr/bin/python3
"""Defines file-writing function."""


def write_file(filename="", text=""):
    """Write string to a text file(UFT8)

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
