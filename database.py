from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#creating the engine for the database connection


engine=create_engine("postgresql://postgres:jeel@localhost/user_competition")

#decalaring the base structure for the creating the tables


Base=declarative_base()

#binding the engine with swssion so that the object can be get and can be provided

SessionLocal= sessionmaker(bind=engine)
