from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update

engine = create_engine('sqlite:///practice.db')

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String)
)
metadata.create_all(engine)

#Insert 3 users
stmt = insert(users).values(name='Alice', email='alice@example.com')
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

#select user
stmt = select(users)
with engine.connect() as conn:
    result = conn.execute(stmt)
    rows = result.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No users found.")

print("Script finished.")


