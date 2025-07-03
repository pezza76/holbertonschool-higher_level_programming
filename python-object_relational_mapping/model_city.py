#!/usr/bin/python3
"""python file that contains the class definition of a city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


# create a class called State the inherits from Base
class City(Base):
    """City class that maps to the 'cities' table in the database."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship('State')
