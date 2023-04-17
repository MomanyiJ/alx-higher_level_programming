#!/usr/bin/python3
""" script taking an argument displaying all values in states table """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    # s is variable name for selecting state instruction
    s = f'SELECT * FROM states WHERE name = "{sys.argv[4]}" ORDER by id ASC'
    cur.execute(s)
    data = cur.fetchall()
    for state in data:
        print(state)

    cur.close()
    db.close()
