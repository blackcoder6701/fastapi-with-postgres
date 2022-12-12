from database import Base
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from competitions.models_comp import Competition
from utils.temp_models import Temp

class Entry(Base,Temp):
    __tablename__ = 'entries'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    status = Column(Boolean)
    country = Column(String)
    state = Column(String)
    comp_id = Column(Integer,ForeignKey("competitions.id"),nullable = False) 
    