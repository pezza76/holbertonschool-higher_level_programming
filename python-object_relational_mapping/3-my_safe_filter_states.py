#!/usr/bin/python3
"""safe input to defend against sql injection"""

import MySQLdb
import sys

# connect to a database
db = MySQLdb.connect(
    host='localhost',
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

# create a cursor object
cur = db.cursor()

query = """
SELECT *
FROM states
WHERE BINARY name = %s;
"""

# run a query
cur.execute(query, (sys.argv[4],))

# fetch results and save them to a variable
result = cur.fetchall()

for i in result:
    print(i)

cur.close()
db.close()
