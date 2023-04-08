import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import aiofiles
import pathlib
import streamlit as st
import pandas as pd
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import plotly
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64,random
import streamlit_authenticator as stauth
import time,datetime
from pymongo import MongoClient
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io,random
import spacy
import nltk
from streamlit_tags import st_tags
from PIL import Image
import io,random
import os
from io  import BytesIO
from PyPDF2 import PdfReader
from pyresparser import ResumeParser
app = FastAPI(title='Untitled', description='doThings', version='0.0.1')


uploads = 'uploads'
uploads_dir = pathlib.Path(os.getcwd(), uploads)

@app.post('/api/upload/')
async def upload_file(file: UploadFile=File(...),file2:UploadFile=File(...)):
    """
    Upload the file to be processed.
    """
    print(file)
#    async with aiofiles.open(file.file, 'rb') as fin:
#       exfile = fin.read() 
    file_name = pathlib.Path(uploads_dir, file.filename)
    async with aiofiles.open(f'{file_name}', 'wb') as f:
        await f.write(await file.read())
    file_name2 = pathlib.Path(uploads_dir, file2.filename)
    async with aiofiles.open(f'{file_name2}', 'wb') as f:
        await f.write(await file2.read())
    #file_name2 = pathlib.Path(uploads_dir, file2.filename) 
    #resume_text = PdfReader('/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/uploads/'+file.filename)
    #jd_text =PdfReader('/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/uploads/'+file2.filename)
    #sume_Analyser_App/uploads/'+file.filename
    #resume_data = ResumeParser(path).get_extracted_data()
    return {"Response":"Successfully uploaded",
            "Resume":file.filename,"Job description":file2.filename,
            "Resume file size":len(file.filename),"Job Description file size":len(file2.filename)}
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4003, log_level='info')