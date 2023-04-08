import uvicorn
from pyresparser import ResumeParser
from fastapi import FastAPI
from pymongo_get_database4 import get_database
from dateutil import parser


from pydantic import BaseModel
class Details(BaseModel):
    name:str
    email:str
    resume_score:str

app = FastAPI()


# After old routes
@app.post('/apiv1-AppSide/')
def api3(data: Details):
    rec=data.dict()
    dbname = get_database()
    collection_name4 = dbname["JobApplicantSide"]

    collection_name4.insert_one(rec)
    return {'message': "Data Updation Successfully for name :" +rec["name"]}

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=4002)