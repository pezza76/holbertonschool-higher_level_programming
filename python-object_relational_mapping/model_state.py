#!/usr/bin/python3
"""python file that contains the class definition of a State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# create the Base class
Base = declarative_base()

# create a class called State the inherits from Base
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
