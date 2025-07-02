import MySQLdb, sys

if __name__ = "__main__":
    #connect to a database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    #Create a cursor object
    cur = db.cursor()

    query = """
    SELECT *
    FROM states
    WHERE name = %s;
    """
    #execute the command
    cur.execute(query, sys.argv[4])

    #save the result
    result = cur.fetchall()

    for i in result:
        print(i)

    #close connections
    cur.close()
    db.close()
