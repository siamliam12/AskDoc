import base64
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session
from typing import List
import shutil
import utils
import models, schemas
from database import SessionLocal, engine
import os
from PyPDF2 import PdfReader 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload-doc")
async def upload_file(file:UploadFile = File(...),db:Session =Depends(get_db)):
    try:
        file_location = f"documents/{file.filename}"
        os.makedirs("documents",exist_ok=True)
        with open(file_location,"wb") as f:
            shutil.copyfileobj(file.file,f)
    finally:
        file.file.close()
     # Create a new document entry in the database
    document_data = {
        "filename": file.filename,
        "file_location": file_location 
    }
    document = schemas.DocumentCreate(**document_data)
    return utils.create_document(db=db,document=document)

@app.post("/questions")
async def handle_questions(query:schemas.QuestionSchema,db:Session = Depends(get_db)):
    data = models.Questions(**query.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"message":f"Question has been saved successfully"}

@app.get("/answer/{id}/{qid}")
async def handle_answer(id:int,qid:int,db:Session = Depends(get_db)):
    name = db.query(models.Pdf).filter(models.Pdf.id==id).first()
    query = db.query(models.Questions).filter(models.Questions.id==qid).first()
    file_location = f"documents/{name.filename}"
    print(file_location)
    #read the file contents
    with open(file_location,"rb") as f:
        pdf = PdfReader(f)
        return {"Answer":utils.read_and_store_document(pdf,query.question,name)}