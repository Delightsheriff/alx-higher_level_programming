#!/usr/bin/python3
"""A script that lists all states from the database"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
       host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
