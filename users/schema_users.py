from pydantic import BaseModel
from typing import List
from database import SessionLocal
from utils.temp_schemas import Temp

#CREATING THE SCHEMAS FOR THE USERS


class Users(BaseModel,Temp):
    """_summary_

    Args:
        BaseModel (_type_): _description_
        Temp (_type_): _description_
    """
    id : int
    name : str
    pass_decrypted : str
    email : str

    class Config:
        """_summary_
        """
        orm_mode = True
