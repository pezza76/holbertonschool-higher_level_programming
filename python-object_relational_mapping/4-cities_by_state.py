#!/usr/bin/python3
"""List all cities of a database"""

import MySQLdb
import sys

if __name__ == '__main__':
    # connect to a database
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # create a cursor object
    cur = db.cursor()

    # write a query
    query = """
    SELECT *
    FROM cities
    ORDER BY id;
    """
    cur.execute(query)

    result = cur.fetchall()

    for i in result:
        print(i)

    cur.close()
    db.close()
