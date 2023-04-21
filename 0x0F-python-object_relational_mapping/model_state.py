#!/usr/bin/python3
"""
Defines a State model.
Inherits from SQLAlchemy base and links to the MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ Represents a state for MySQL database.
    Attributes:
        __tablename__ (str): name of MySQL table
        id (sqlachemy.String): State's name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
