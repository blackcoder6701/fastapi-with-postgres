from database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from utils.temp_models import Common_class

#creating the model for the competition
#here the id --> primary key
#here the user_id  --> foreign key (it refers the user table)
class Competition(Base,Common_class):
    """cerating the class for the competitions

    Args:
        Base (_type_): _description_
        Common_class (_type_): _description_
    """
    __tablename__ = 'competitions'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    status = Column(Boolean,default=False)
    url = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"),nullable = False)
