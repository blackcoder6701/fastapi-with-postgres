from fastapi import APIRouter,Depends
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from entry.schemas_entry import Entries
from entry.models_entry import  Entry

entryRouter = APIRouter()

db = SessionLocal() 

@entryRouter.get('/entry')
def entries_homepage():
    list_of_entry = db.query(Entry).all()
    return list_of_entry
    
@entryRouter.get('/entry/{entry_id}')
def competitons_id(entry_id:int):
    
    desired_item = db.query(Entry).filter(Entry.id == entry_id).first()
    
    return desired_item


@entryRouter.post('/entries',response_model=Entries,status_code=201)
def post_entries(entry:Entries):
    new_entry = Entry(
        id = entry.id,
        name = entry.name,
        status = entry.status,
        country = entry.country,
        state = entry.state,
        comp_id = entry.comp_id
    )
    
    db.add(new_entry)
    db.commit()
    
    return new_entry

    
@entryRouter.put('/entry/{entry_id}')
def put_update(entry_id:int,entry:Entries):
        update = db.query(Entry).filter(Entry.id == entry_id).first()
        update.name = entry.name,
        update.country = entry.country,
        update.state = entry.state,
        update.comp_id = entry.comp_id
        
        db.commit()
        
        return update
        
        
@entryRouter.delete('/entry/{entry_id}')
def delete_compe(entry_id:int):
    delete_id = db.query(Entry).filter(Entry.id == entry_id).first()
    db.delete(delete_id)
    db.commit()
    print(delete_id)
    return delete_id