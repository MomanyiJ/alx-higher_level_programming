#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db= MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute('SELECT * FROM states ORDER BY id ASC')
    data = curr.fetchall()
    for state in data:
        print(state)

    curr.close()
    db.close()
