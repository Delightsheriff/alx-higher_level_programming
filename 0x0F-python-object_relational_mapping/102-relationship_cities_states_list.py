#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    x = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    y = pool_pre_ping = True
    engine = create_engine(x.format(argv[1], argv[2], argv[3]), y)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).join(City).order_by(City.id).all()

    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
