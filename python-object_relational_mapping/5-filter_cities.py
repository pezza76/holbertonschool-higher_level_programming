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

    # create a curso object
    cur = db.cursor()

    # create the sql query
    query = """
    select cities.name
    from cities
    join states on cities.state_id = states.id
    where states.name = %s
    order by cities.id;
    """
    # execute the query
    cur.execute(query, (sys.argv[4],))

    #fetch the results and save to a variable
    result = cur.fetchall()

    for i in result:
        print(i[0], end=", ")

    cur.close()
    db.close()
