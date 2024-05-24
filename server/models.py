from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from database import Base

class Pdf(Base):
    __tablename__ = 'pdf'
    id = Column(Integer, primary_key=True,index=True,autoincrement=True)
    filename = Column(String)
    file_location = Column(String)
    upload_date = Column(DateTime, default=datetime.now())

class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True,index=True,autoincrement=True)
    pdf_id = Column(String)
    question = Column(String)
    created_at = Column(DateTime, default=datetime.now())