import uvicorn
from dotenv import load
import os

load()

if __name__=="__main__":
    Host=os.getenv("HOST")
    Port=os.getenv("PORT")
    uvicorn.run("api.main:app",host=Host,port=int(Port),reload=True)
