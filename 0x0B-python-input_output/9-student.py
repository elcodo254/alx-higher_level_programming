#!/usr/bin/python3
"""Define class Student"""


class Student:
    """Represents student"""

    def __init__(self, first_name, last_name, age):
        """initialize new student

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get dict representation of the student """
        return self.__dict__
