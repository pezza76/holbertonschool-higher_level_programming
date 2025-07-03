from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Create a Base class
Base = declarative_base()

# Define a table using a python class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# connect to a database
engine = create_engine('sqlite:///mydb3.db')

# build all tables (this tells the base class to build tables in that database passed to engine)
Base.metadata.create_all(engine)

# create a session to work with the data
Session = sessionmaker(bind=engine)
session = Session()

# insert some data
session.add_all([
    User(name='Kim', email='kim@example.com'),
    User(name='Andy', email='Andy@hotmail.com')
])

# update values
user = session.query(User).filter_by(name='Kim').first()
user.name = 'Tim'

# save session
session.commit()

# create a query
users = session.query(User).all()

# print out the query
for user in users:
    print(user.name)

user_to_delete = session.query(User).filter_by(name='Andy').first()
if user_to_delete:
    session.delete(user_to_delete)
session.commit()

users = session.query(User).all()
for user in users:
    print(user.name, user.email)