#!/usr/bin/python3
""" scrip listing cities from the database """

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    # s denotes variable named script
    s = "SELECT cities.id, cities.name, states.name FROM cities \
LEFT OUTER JOIN states ON cities.state_id=states.id \
ORDER BY cities.id ASC"
    cur.execute(s)
    data = cur.fetchall()
    for row in data:
        print(row)

    cur.close()
    db.close()
