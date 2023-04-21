#!/usr/bin/python3
"""
Defines a City model.
Inherits from SQLAlchemy base and links to the MySQL table citiess
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Represents a city for MySQL database.
    __tablename__(str): name of MySQL table

    Attributes:
        id (string): City id
        name(sqlalchemy.Integer): City name
        state_id (sqlachemy.String): State id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
