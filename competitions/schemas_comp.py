from pydantic import BaseModel
from typing import List
from database import SessionLocal
from utils.temp_schemas import Temp

class Competitions(BaseModel,Temp):
    id : int
    name :str
    status : bool
    url : str
    user_id : int
    
    class Config:
        orm_mode = True