#!/usr/bin/python3
"""Delete states containing the letter 'a'"""

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

    # find states containing the letter a
    states = session.query(State).filter(State.name.like('%a%')).all()
 
    # delete these states
    for state in states:
        session.delete(state)

    session.commit()
