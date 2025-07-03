#!/usr/bin/python3
"""Add Louisiana to the database"""

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

    # insert item
    session.add(State(name='Louisiana'))
    session.commit()

    # create a query
    states = session.query(State).all()

    # print result
    for state in states:
        print(f"{state.id}: {state.name}")
