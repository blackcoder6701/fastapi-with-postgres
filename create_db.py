from database import Base, engine
from entry.models_entry import  Entry
from competitions.models_comp import Competition
from users.models_users import User

Base.metadata.create_all(engine)

print("creating the database...")
