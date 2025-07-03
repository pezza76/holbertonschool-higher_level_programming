#!/usr/bin/python3
"""python file that prints all state entered by user"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create a query
    state = session.query(State).filter_by(name=sys.argv[4]).first()

    # print result
    if state:
        print(state.id)
    else:
        print('Not found')
