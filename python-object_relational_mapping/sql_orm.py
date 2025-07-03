from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


engine = create_engine('sqlite:///mydb.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    User(name="Bob", email="bob@example.com"),
    User(name="Eve", email="eve@example.com")
])
session.commit()



user = session.query(User).filter_by(name='Bob').first()
user.name = 'Dude'
session.commit()

users = session.query(User).all()

for user in users:
    print(user.name)

