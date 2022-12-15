from database import Base
from sqlalchemy import Column,String,Integer,Boolean



class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    pass_decrypted=Column(String)
    is_deleted=Column(Boolean)
    email=Column(String)
    created_at=Column(Integer)
    created_by=Column(String)
    updated_at=Column(Integer)
    updated_by=Column(String)



class Competition(Base):
    __tablename__='competitions'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    status=Column(Boolean)
    url=Column(String)
    is_deleted=Column(Boolean)
    created_at=Column(Integer)
    updated_at=Column(Integer)
    user_id=Column(Integer)


class Entry(Base):
    __tablename__='Entry'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    status=Column(Boolean)
    country=Column(String)
    state=Column(String)
    is_deleted=Column(Boolean)
    created_at=Column(Integer)
    updated_at=Column(Integer)
    comp_id=Column(Integer)
