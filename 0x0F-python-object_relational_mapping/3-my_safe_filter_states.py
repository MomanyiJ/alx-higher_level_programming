#!/usr/bin/python3
""" SQL injection protection """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    if ' ' not in sys.argv[4]:
        s = 'SELECT * FROM states WHERE BINARY name = "{}" ORDER by id ASC'
        cur.execute(s.format(sys.argv[4]))
        data = cur.fetchall()
        for state in data:
            print(state)

    cur.close()
    db.close()
