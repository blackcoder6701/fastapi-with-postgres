from fastapi import APIRouter,Depends
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from entry.schemas_entry import Entries
from entry.models_entry import  Entry
from competitions.models_comp import Competition

entryRouter = APIRouter()

db = SessionLocal()

#creating the routes for the entry table
@entryRouter.get('/entry')
def entries_homepage():
    """_summary_

    Returns:
        _type_: _description_
    """
    list_of_entry = db.query(Entry).all()
    return list_of_entry

@entryRouter.get('/entry/{entry_id}')
def competitons_id(entry_id:int):
    """_summary_

    Args:
        entry_id (int): _description_

    Returns:
        _type_: _description_
    """

    desired_item = db.query(Entry).filter(Entry.id == entry_id).first()

    return desired_item


@entryRouter.post('/entries',response_model=Entries,status_code=201)
def post_entries(entry:Entries):
    """_summary_

    Args:
        entry (Entries): _description_

    Returns:
        _type_: _description_
    """
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
    """_summary_

    Args:
        entry_id (int): _description_
        entry (Entries): _description_

    Returns:
        _type_: _description_
    """
    update = db.query(Entry).filter(Entry.id == entry_id).first()
    update.name = entry.name,
    update.country = entry.country,
    update.state = entry.state,
    update.comp_id = entry.comp_id

    db.commit()

    return update


@entryRouter.delete('/entry/{entry_id}')
def delete_compe(entry_id:int):
    """_summary_

    Args:
        entry_id (int): _description_

    Returns:
        _type_: _description_
    """
    delete_id = db.query(Entry).filter(Entry.id == entry_id).first()
    db.delete(delete_id)
    db.commit()
    print(delete_id)
    return delete_id


@entryRouter.get('/entry/{user_id}/count')
def count_user(user_id:int):
    """_summary_

    Args:
        user_id (int): _description_

    Returns:
        _type_: _description_
    """

    competitions = db.query(Competition.id).filter(Competition.user_id == user_id).all()
    # return competitons

    competitons_id = [competition.id for competition in competitions]
    # return competitons_id

    final_ans= 0
    for competition_id in competitons_id:
        entry = db.query(Entry.id).filter(Entry.comp_id==competition_id).count()

        final_ans += entry
    return final_ans
