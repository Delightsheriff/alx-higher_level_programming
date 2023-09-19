#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    temp = """
        SELECT
            cities.id, cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name LIKE BINARY %(state_name)s
        ORDER BY
            cities.id ASC
        """
    cur.execute(temp, (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
