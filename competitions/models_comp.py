from database import Base
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from users.models_users import User
from utils.temp_models import Common_class

#creating the model for the competition
#here the id --> primary key
#here the user_id  --> foreign key (it refers the user table)

class Competition(Base,Common_class):
    """_summary_

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
