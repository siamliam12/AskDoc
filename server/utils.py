from sqlalchemy.orm import Session 
import models,schemas


def create_document(db:Session,document:schemas.DocumentCreate):
    db_document = models.Pdf(filename=document.filename,content=document.content)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document