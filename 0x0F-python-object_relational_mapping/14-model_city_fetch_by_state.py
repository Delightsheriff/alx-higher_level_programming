#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    temp = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(temp)
    Session = sessionmaker(bind=engine)
    session = Session()

    final = session.query(City, State).join(State)

    for city, state in final.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
