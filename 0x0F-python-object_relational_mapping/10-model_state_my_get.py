#!/usr/bin/python3

"""Script printing State object with its name paased
as an argument fro the DB hbtn_0e_6_usa
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # takes these 4 command line arguments
    username, password, database_name, \
        state_name = argv[1], argv[2], argv[3], argv[4]

    # connection to db using mysql server on local host at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)

    # make a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query state name
    results = session.query(State).filter(State.name == state_name).first()

    # print stae ID or not found if it does not exist
    if results is None:
        print("Not Found")
    else:
        print(results.id)
