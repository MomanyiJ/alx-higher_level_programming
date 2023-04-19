#!/usr/bin/python3

from sqlalchemy import String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Represents a State in US.

    Attributes include
    id(int): unique state identifier
    name(str): Name of stae
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
# connect to MySQL server
#engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/mydatabase')

#Base.metadat.create_all(engine)
