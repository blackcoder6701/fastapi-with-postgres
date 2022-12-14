from fastapi import APIRouter, Depends
from database import SessionLocal
from competitions.models_comp import Competition
from competitions.schemas_comp import Competitions
from sqlalchemy.orm import Session
from utils.db import get_db 
compRouter = APIRouter()



#creating the routes for the Competitions
@compRouter.get('/competitions')
def competitions_homepage(db: Session = Depends(get_db)):
    """_getting the all competitions

    Returns:
        _type_: _description_
    """    
    list_of_comp = db.query(Competition).all()
    return list_of_comp

@compRouter.get('/competitions/{comp_id}')
def competitons_id(comp_id:int,db: Session = Depends(get_db)):
    """getting the competitions through id

    Args:
        comp_id (int): _description_

    Returns:
        _type_: _description_
    """    
    desired_item = db.query(Competition).filter(Competition.id == comp_id).first()
    print(desired_item)
    return {
        "id": desired_item.id,
        "name": desired_item.name,
        "url": desired_item.url
    }

@compRouter.post('/competitions',response_model=Competitions,status_code=201)
def post_competitions(comp:Competitions,db: Session = Depends(get_db)):
    """_posting in the competitions

    Args:
        comp (Competitions): _description_

    Returns:
        _type_: _description_
    """
    new_comp = Competition(
        id = comp.id,
        name = comp.name,
        status = comp.status,
        url = comp.url,
        user_id = comp.user_id
    )
    db.add(new_comp)
    db.commit()
    return new_comp

@compRouter.put('/competitions/{compe_id}')
def put_update(compe_id:int,comp:Competitions,db: Session = Depends(get_db)):
    """upadating the existing comp's

    Args:
        compe_id (int): _description_
        comp (Competitions): _description_

    Returns:
        _type_: _description_
    """
    update = db.query(Competition).filter(Competition.id==compe_id).first()
    update.name = comp.name,
    update.url = comp.url,

    db.commit()
    return update

@compRouter.delete('/competitions/{compe_id}')
def delete_compe(compe_id : int,db: Session = Depends(get_db)):
    """deleting the existing comps through id  

    Args:
        compe_id (int): _description_

    Returns:
        _type_: _description_
    """
    delete_id = db.query(Competition).filter(Competition.id == compe_id).first()
    db.delete(delete_id)
    db.commit()
    return delete_id
