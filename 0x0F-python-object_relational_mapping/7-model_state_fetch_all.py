#!/usr/bin/python3
"""
lists all state objects
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    """get credentials"""
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    """create a connection string and engine"""
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}")

    """create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Get all states"""
    states = session.query(State).order_by(State.id).all()

    """print each state's id and name"""
    for state in states:
        print(f"{state.id}: {state.name}")
