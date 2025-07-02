from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String


#connect to a database
engine = create_engine('sqlite:///practice.db')

#create a folder that stores the table blueprints
metadata = MetaData()

#Define a Table
users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String)
)
#create table if it doesn't exist
metadata.create_all(engine)