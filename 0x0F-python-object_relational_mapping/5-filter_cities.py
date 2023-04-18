#!/usr/bin/python3
""" script taking state name as 
argument lisitng all cities of that state from
 hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    if ' ' not in sys.argv[4]:
        s = 'SELECT cities.name FROM cities {} {} "{}" {}'.format(
            'JOIN states ON cities.state_id=states.id',
            'WHERE states.name LIKE', sys.argv[4],
            'ORDER BY cities.id ASC')
        cur.execute(s)
        data = cur.fetchall()
        states = ", ".join(row[0] for row in data)
        print(states)

    cur.close()
    db.close()


