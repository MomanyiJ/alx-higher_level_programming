#!/usr/bin/python3

""" script printing first State object from the db
hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username, password, database_name = argv[1], argv[2], argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create sessions
    Session = sessionmaker(bind=engine)
    session = Session()

    # query for first object from the DB
    states = session.query(State).order_by(State.id).first()
    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
