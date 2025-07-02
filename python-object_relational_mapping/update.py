from sqlalchemy import update
from db import users, engine

up = (update(users)
.where(users.c.name=='Andrew')
.values(name='Yeimy')
)

with engine.connect() as conn:
    conn.execute(up)
    conn.commit()