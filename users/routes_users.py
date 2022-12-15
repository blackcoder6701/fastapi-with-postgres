from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from users.models_users import User
from users.schema_users import Users


userRoute = APIRouter()
"""_summary_

    Returns:
        _type_: _description_
    """

db = SessionLocal()

#CREATING THE ROUTES FOR THE USERS TABLE


@userRoute.get('/users',response_model=List,status_code=200)
def users_homepage():
    """_summary_

    Returns:
        _type_: _description_
    """
    items=db.query(User).all()
    return [{"id": item.id, "name": item.name, "email": item.email} for item in items]


@userRoute.get('/users/{user_id}')
def get_by_user(user_id):
    """_summary_

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
def post_details(user:Users):
    """_summary_

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
def update_data(user_id:int,user:Users):
    """_summary_

    Args:
        user_id (int): _description_
        user (Users): _description_

    Returns:
        _type_: _description_
    """
    update=db.query(User).filter(User.id==user_id).first()
    update.name = user.name,
    update.pass_decrypted = user.pass_decrypted,
    update.email = user.email,

    db.commit()
    return update


@userRoute.delete('/users/{user_id}')
def delete_data(user_id:int):
    """_summary_

    Args:
        user_id (int): _description_

    Returns:
        _type_: _description_
    """
    user_to_delete = db.query(User).filter(User.id == user_id).first()


    db.delete(user_to_delete)
    db.commit()

    return user_to_delete
