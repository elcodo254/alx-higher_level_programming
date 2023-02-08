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

    def to_json(self, attrs=None):
        """get dict representation of the student
        if  attrs is a list of strings, only attribute names
        contained in this list must be retrieved

        Args:
            attrs (list): (optional) attributes to rep
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
