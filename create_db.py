from database import Base,engine
from models import User,Competition,Entry


Base.metadata.create_all(engine)



print("hold your breath ")
print("creating the database...")