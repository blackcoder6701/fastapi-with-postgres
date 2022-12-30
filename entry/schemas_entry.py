from pydantic import BaseModel
from utils.temp_schemas import Temp

#creating the schemas for the Entry table
class Entries(BaseModel,Temp):
    id : int
    name : str
    status : bool
    country : str
    state : str
    comp_id : int

    class Config:
        orm_mode = True
