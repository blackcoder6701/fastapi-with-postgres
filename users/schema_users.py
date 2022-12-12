from pydantic import BaseModel
from typing import List
from database import SessionLocal
from utils.temp_schemas import Temp


class Users(BaseModel,Temp):
    id:int
    name:str
    pass_decrypted:str
    email:str
    
    class Config:
        orm_mode=True