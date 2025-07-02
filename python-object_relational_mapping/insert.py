from sqlalchemy import insert
from db import engine, users

sd = insert(users).values([
    {'name': 'Alice', 'email': 'alice@example.com'},
    {'name': 'Andrew', 'email': 'pezza76@hotmai.com'}
])

with engine.connect() as conn:
    conn.execute(sd)
    conn.commit()