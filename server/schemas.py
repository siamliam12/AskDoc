from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PdfSchema(BaseModel):
    id:Optional[int] = None
    filename: str
    content: str

class DocumentCreate(PdfSchema):
    filename: str
    content: str

class Document(PdfSchema):
    id:Optional[int] = None
    upload_date: datetime
    class Config:
        orm_mode = True