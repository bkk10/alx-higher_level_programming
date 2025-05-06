#!/usr/bin/python3
"""
list the first state
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    """create a connection"""
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}")

    """create a session to run on engine"""
    Session = sessionmaker(bind=engine)
    session = Session()

    delete_data = session.query(State).filter(State.name.like('%a')).all()

    for states in delete_data:
        session.delete(states)
    session.commit()

    session.close()

