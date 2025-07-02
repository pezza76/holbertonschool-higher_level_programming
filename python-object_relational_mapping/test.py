import MySQLdb

#connect to a database
db = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='hbtn_0d_tvshows'
)

#create a cursor to allow you to execute sql demands
cursor = db.cursor()

#run this command
cursor.execute("SHOW TABLES;")

#get results
x = cursor.fetchall() #this returns a tuple

for i in x:
    print(i[0])






