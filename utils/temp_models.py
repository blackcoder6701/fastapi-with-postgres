from sqlalchemy import Column,Boolean,String,DateTime
import datetime
import getpass



class Temp(object):
    is_deleted = Column(Boolean,default = False)
    created_at = Column(DateTime ,default = datetime.datetime.utcnow)
    created_by = Column(String,default = getpass.getuser())
    updated_at = Column(DateTime,nullable = True, onupdate = datetime.datetime.utcnow)
    updated_by = Column(String,nullable = True)