from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List, Optional


class TagCreate(BaseModel):
    name: str

class TagDisplay(BaseModel):
    id: UUID
    name: str

class ArticleCreate(BaseModel):
    title: str
    text: str
    created: Optional[datetime]
    tags: Optional[List[object]]

class ArticleDisplay(BaseModel):
    id: UUID
    title: str
    text: str
    created: str
    tags: Optional[List[object]]
    class Config():
        orm_mode = True
        
class NotesDisplay(BaseModel):
    id: UUID
    text: str
    created: str
    class Config():
        orm_mode = True

class NoteCreate(BaseModel):
    text: str
    created: Optional[datetime]