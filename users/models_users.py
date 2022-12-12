from database import Base
from sqlalchemy import Column,String,Integer,Boolean
from utils.temp_models import Temp


class User(Base,Temp):
    __tablename__ = 'users'
    id = Column(Integer,primary_key = True)
    name = Column(String)
    pass_decrypted = Column(String)
    email = Column(String)
    
    

