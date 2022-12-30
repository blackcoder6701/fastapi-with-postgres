from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from users.models_users import User
from users.schema_users import Users
from sqlalchemy.orm import Session
from utils.db import get_db

userRoute = APIRouter()
"""creating the route

    Returns:
        _type_: _description_
    """
#CREATING THE ROUTES FOR THE USERS TABLE
@userRoute.get('/users',response_model=List,status_code=200)
def users_homepage(db: Session = Depends(get_db)):
    """homepage display

    Returns:
        _type_: _description_
    """
    items = db.query(User).all()
    return [{"id": item.id, "name": item.name, "email": item.email} for item in items]

@userRoute.get('/users/{user_id}')
def get_by_user(user_id,db: Session = Depends(get_db)):
    """getting the user through id

    Args:
        user_id (_type_): _description_
    """
    user_get=db.query(User).filter(User.id == user_id).first()
    return{
        "id" : user_get.id,
        "name" : user_get.name,
        "pass_decrypted" : user_get.pass_decrypted,
        "email" : user_get.email
    }

@userRoute.post('/users/',response_model=Users,status_code=201)
def post_details(user:Users,db: Session = Depends(get_db)):
    """function for posting the details

    Args:
        user (Users): _description_

    Returns:
        _type_: _description_
    """
    one_user = User(
        id = user.id,
        name = user.name,
        pass_decrypted = user.pass_decrypted,
        email = user.email,
    )

    db.add(one_user)
    db.commit()
    return one_user

@userRoute.put('/users/{user_id}')
def update_data(user_id:int,user:Users,db: Session = Depends(get_db)):
    """for the modification of the details
    Args:
        user_id (int): _description_
        user (Users): _description_

    Returns:
        _type_: _description_
    """
    update = db.query(User).filter(User.id==user_id).first()
    update.name = user.name,
    update.pass_decrypted = user.pass_decrypted,
    update.email = user.email,

    db.commit()
    return update

@userRoute.delete('/users/{user_id}')
def delete_data(user_id : int):
    """for the deletion of the routes

    Args:
        user_id (int): _description_

    Returns:
        _type_: _description_
    """
    user_to_delete = db.query(User).filter(User.id == user_id).first()
    
    db.delete(user_to_delete)
    db.commit()

    return user_to_delete
