from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import TagDisplay
from typing import List, Optional
from db.database import get_db
from db.models import Tag


router = APIRouter(prefix='/tags', tags=['tags'])

@router.get('/')
def get_all_notes(db: Session = Depends(get_db)):
    return db.query(Tag).all()