#!/usr/bin/python3

"""
scri[t lisitng all state objects containgin letter 'a'
from the the DB hbtn_0e_6_usa
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

    Session = sessionmaker(bind=engine)
    session = Session()

    # query DB for states with 'a'
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    # print(states)

    # for loop for printing results
    for state in states:
        print("{}: {}".format(state.id, state.name))
