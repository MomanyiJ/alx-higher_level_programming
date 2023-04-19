#!/usr/bin/python3
""" 
Script lisiting State Objects from the DB hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine

if __name__ == "__main__":
    # assigning variables
    username, password, database = argv[1], argv[2], argv[3]
    # connect to DB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(username, password, database),
                            pool_pre_ping=True)
    # Base.metadata.create_all(engine)

    # session creation
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # query all objects fromState and sorted by id in ascending order
    states = session.query(State).order_by(State.id).all()

    #prints the results

    for state in states:
        print('{}: {}'.format(state.id, state.name))
