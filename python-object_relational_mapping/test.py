from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books' # this line tells it to connect to a table called books in the database
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

print(Base.metadata.tables)

