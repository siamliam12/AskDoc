from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from database import Base

class Pdf(Base):
    __tablename__ = 'pdf'
    id = Column(Integer, primary_key=True,index=True,autoincrement=True)
    filename = Column(String)
    content = Column(String)
    upload_date = Column(DateTime, default=datetime.now())