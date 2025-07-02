from sqlalchemy import select
from db import engine, users

sl = select(users)

with engine.connect() as conn:
    result = conn.execute(sl)
    for row in result:
        print(row)