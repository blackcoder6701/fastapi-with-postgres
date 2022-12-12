from database import Base
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from users.models_users import User
from utils.temp_models import Temp


class Competition(Base,Temp):
    __tablename__ = 'competitions'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    status = Column(Boolean,default=False)
    url = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"),nullable = False)
   
    
    