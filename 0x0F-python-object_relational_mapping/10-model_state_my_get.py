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
    state_name = sys.argv[4]

    """create a connection"""
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}")

    """create a session to run on engine"""
    Session = sessionmaker(bind=engine)
    session = Session()

    name_search = session.query(State).filter(State.name == state_name).first()

    if name_search:
        print(name_search.id)
    else:
        print("Not found")
