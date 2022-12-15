from pydantic import BaseModel
from typing import List
from database import SessionLocal
from utils.temp_schemas import Temp


#creating the schemas for the Competitions

class Competitions(BaseModel,Temp):
    """_summary_

    Args:
        BaseModel (_type_): _description_
        Temp (_type_): _description_
    """
    id : int
    name :str
    status : bool
    url : str
    user_id : int

    class Config:
        orm_mode = True
