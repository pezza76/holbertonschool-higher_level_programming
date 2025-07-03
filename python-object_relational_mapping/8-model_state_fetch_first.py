#!/usr/bin/python3
"""python file that contains the class definition of a State"""

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
    first = session.query(State).first()

    for state in first:
        print(f"{state.id}: {state.name}")
