#!/usr/bin/python3
""" using SQL alchemy """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column
from sqlalchemy import create_engine

Base = declarative_base()


# Definig the class
class State(Base):
    """ State table """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user = Column(String(128), nullable=False)
