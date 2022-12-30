from database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from utils.temp_models import Common_class


#creating the Entry model for the table creation
#here the comp_id --> foriegn  key(for the mapping the comp table)
class Entry(Base,Common_class):
    """creating the model for the entry
    Args:
        Base (_type_): _description_
        Common_class (_type_): _description_
    """
    __tablename__ = 'entries'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    status = Column(Boolean)
    country = Column(String)
    state = Column(String)
    comp_id = Column(Integer,ForeignKey("competitions.id"),nullable = False)
