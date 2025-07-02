from sqlalchemy import delete
from db import users, engine

dl = (delete(users)
       .where(users.c.name=='Alice')
)

with engine.connect() as conn:
    conn.execute(dl)
    conn.commit()