#!/usr/bin/python3
"""
script adding State object Louisiana to the hbtn_0e_6_usa DB
"""

from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":

    # takes 3 arguments username, password database_name
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    # connection to MySQL server running localhost through 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)

    # make session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create new state object "Louisianna"
    new_state = State(name='Louisiana')

    # add to the session and commit it
    session.add(new_state)
    session.commit()

    # print new State's object ID
    print(new_state.id)
