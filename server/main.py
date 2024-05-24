import base64
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session
from typing import List
import shutil
import utils
import models, schemas
from database import SessionLocal, engine
import os

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
        # contents = file.file.read()
        file_location = f"documents/{file.filename}"
        os.makedirs("documents",exist_ok=True)
        with open(file_location,"wb") as f:
            shutil.copyfileobj(file.file,f)
    finally:
        file.file.close()
     # Create a new document entry in the database
    document_data = {
        "filename": file.filename,
        "content": file_location # You can modify this to store actual content if needed
    }
    document = schemas.DocumentCreate(**document_data)
    return utils.create_document(db=db,document=document)

@app.post("/questions")
def handle_questions():
    pass