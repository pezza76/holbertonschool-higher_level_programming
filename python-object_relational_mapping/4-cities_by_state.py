#!/usr/bin/python3
"""List all cities of a database"""

import MySQLdb
import sys

# connect to a database
db = MySQLdb.connect(
    host='localhost',
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

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
