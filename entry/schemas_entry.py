from pydantic import BaseModel
from typing import List
from database import SessionLocal

from utils.temp_schemas import Temp

class Entries(BaseModel,Temp):
    id : int
    name : str
    status : bool
    country : str
    state : str
    comp_id : int
    
    class Config:
        orm_mode = True