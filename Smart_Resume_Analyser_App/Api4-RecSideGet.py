from git import List
import uvicorn
from pyresparser import ResumeParser
from fastapi import APIRouter, FastAPI
from pymongo_get_database import get_database
from dateutil import parser
from bson import ObjectId

from pydantic import BaseModel, Field
from pymongo import MongoClient
from typing import Optional
from pydantic import BaseModel, Field

client = MongoClient()
db = client.user5

app = FastAPI()
dbname = get_database()
collection_name = dbname["user5"]

class User(BaseModel):
    name : str
    email:str
    resume_score:str
    time_of_update:str
    actual_skill:str
    predicted_field:str
    skills_recommended:str
    courses_recommended:str

def user_serializer(user) -> dict:
    return {
    'id':str(user["_id"]),
    'name':user["name"],
    'email':user["email"],
            'resume_score':user["resume_score"],
            'time_of_update':user["time_of_update"],
            'actual_skill':user["actual_skills"],
            'predicted_field':user["predicted_field"],
            'skills_recommended':user["skills_recommended"],
            'courses_recommended':user["courses_recommended"], 
}


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]
user = APIRouter()

@app.get("/")
async def find_all_users():
    users = users_serializer(collection_name.find())
    return {"status": "Ok","data": users}


if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=4004)