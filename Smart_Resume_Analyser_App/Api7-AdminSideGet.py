from git import List
import uvicorn
from pyresparser import ResumeParser
from fastapi import APIRouter, FastAPI
from pymongo_get_database3 import get_database
from dateutil import parser
from bson import ObjectId

from pydantic import BaseModel, Field
from pymongo import MongoClient
from typing import Optional
from pydantic import BaseModel, Field


client = MongoClient()
db = client.JobApplicantSide

app = FastAPI()
dbname = get_database()
collection_name3 = dbname["Admin"]

class User(BaseModel):
    Username:str
    Password:str
    Page_Authorised:str
    Hashed_Password:str

def user_serializer(user) -> dict:
    return {
    'id':str(user["_id"]),
    'Username':user["Username"],
    'Password':user["Password"],
    'Page_Authorised':user["Page_Authorised"],
    'Hashed_Password':user["Hashed_Password"]
}


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]
user = APIRouter()

@app.get("/")
async def find_all_users():
    users = users_serializer(collection_name3.find())
    return {"status": "Ok","data": users}


if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=4007)