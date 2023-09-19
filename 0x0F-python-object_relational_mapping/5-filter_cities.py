#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    temp = """SELECT cities.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        WHERE states.name=%s
        ORDER BY cities.id ASC"""
    cur.execute(temp, (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
