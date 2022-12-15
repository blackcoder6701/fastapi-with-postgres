#importing the necessary libraries

from fastapi import FastAPI
from users.routes_users import userRoute
from competitions.routes_comp import compRouter
from entry.routes_entry import entryRouter



#created the instance
app=FastAPI()

#Creating the subroutes
"""_summary_

    Returns:
        _type_: _description_
    """
app.include_router(userRoute)
app.include_router(compRouter)
app.include_router(entryRouter)






@app.get('/')
def home():
    return {"data":"you are at the home page"}
