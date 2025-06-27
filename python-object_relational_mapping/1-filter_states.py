#!/usr/bin/python3
"""Module that lists all states with a name starting with 'N' from the database."""

import MySQLdb
import sys

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

query = """
SELECT name
FROM states
WHERE name LIKE'N%'
ORDER BY states.id;
"""

cur = db.cursor()

cur.execute(query)
result = cur.fetchall()

for i in result:
    print(i)
