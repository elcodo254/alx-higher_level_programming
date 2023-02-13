#!/usr/bin/python3
"""Define a base model class"""

class Base:
    """Represents the base model for all classes in project

    Attributes:
        __nb__objects (int): The number of instatiated Bases
    """

    def __init__(self, id=None):
        """Initialize a new base

        Args:
            id (int): Identity of new base
        """
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base.__nb__objects
