from fastapi import FastAPI, Depends
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
#from app.dependencies import get_db
#from app.db.models.users import User
#from app.api import vendors, workorders, workorder_items, invoices, contractors, me

app = FastAPI()

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello, World!"}

# @app.get("/users")
# def list_users(db: Session = Depends(get_db)):
#     return db.query(User).all()
# from sqlalchemy import create_engine
# # from sqlalchemy.pool import NullPool
# from dotenv import load_dotenv
# import os

# Load environment variables from .env
#load_dotenv()

# Fetch variables
# USER = os.getenv("user")
# PASSWORD = os.getenv("password")
# HOST = os.getenv("host")
# PORT = os.getenv("port")
# DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
# DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
# engine = create_engine(DATABASE_URL)
# try:
#     with engine.connect() as connection:
#         print("Connection successful!")
# except Exception as e:
#     print(f"Failed to connect: {e}")
    
    
    
    
    


# app.include_router(me.router)
# app.include_router(vendors.router)
# app.include_router(workorders.router)
# app.include_router(workorder_items.router)
# app.include_router(invoices.router)
# app.include_router(contractors.router)
