from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PdfSchema(BaseModel):
    id:Optional[int] = None
    filename: str
    file_location: str

class DocumentCreate(PdfSchema):
    filename: str
    file_location: str

class Document(PdfSchema):
    id:Optional[int] = None
    upload_date: datetime
    class Config:
        from_attributes = True

class QuestionSchema(BaseModel):
    id:Optional[int] = None
    pdf_id :str
    question : str
    created_at :datetime