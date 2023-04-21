#!/usr/bin/python3
"""
Defines a State model.
Inherits from SQLAlchemy base and links to the MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """ Represents a state for MySQL database.
    Attributes:
        __tablename__ (str): name of MySQL table
        id (sqlachemy.String): State id
        name(sqlalchemy.String): state name.
        cities (sqlalchemy.orm.relationship): The State-City relationship
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
