import uvicorn
from pyresparser import ResumeParser
from fastapi import FastAPI
from pymongo_get_database3 import get_database
from dateutil import parser


from pydantic import BaseModel
class Details(BaseModel):
    Username:str
    Password:str
    Page_Authorised:str
    Hashed_Password:str

app = FastAPI()


# After old routes
@app.post('/')
def api3(data: Details):
    rec=data.dict()
    dbname = get_database()
    collection_name3 = dbname["Admin"]

    collection_name3.insert_one(rec)
    return {'message': "Data Updation Successfully for name :" +rec["Username"]}

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=4006)