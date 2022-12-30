from sqlalchemy import Column,Boolean,String,DateTime
import datetime
import getpass
from database import Base

def dtnew():
    return datetime.datetime.utcnow

class Common_class():
    """common  class is created so that the 

    Args:
        object (_type_): _description_
    """
    is_deleted = Column(Boolean,default = False)
    created_at = Column(DateTime ,default = dtnew())
    created_by = Column(String,default = getpass.getuser())
    updated_at = Column(DateTime,nullable = True, onupdate = dtnew())
    updated_by = Column(String,nullable = True)


