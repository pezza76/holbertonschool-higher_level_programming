from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# set up the Base class
Base = declarative_base()

# define a table as an instance of a class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# connect to a database
engine = create_engine('sqlite:///mydb2.db')

# build the table
Base.metadata.create_all(engine)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into table
session.add_all([
    User(name='zed', email='xxx@example.com'),
    User(name='Tom', email="zez@example.com")
]
)

# update data
user = session.query(User).filter_by(name='zed').first()
user.name = 'Brian'

session.commit()

users = session.query(User).all()

for user in users:
    print(user.name)
