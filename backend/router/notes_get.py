from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import NotesDisplay
from typing import List, Optional
from db.database import get_db
from db.models import Note


router = APIRouter(prefix='/notes', tags=['notes'])

@router.get('/')
def get_all_notes(limit: Optional[int] = 3, page: Optional[int] = 1, db: Session = Depends(get_db)):
    total_notes = db.query(Note).count()
    total = total_notes // limit
    if total_notes % limit > 0:
        total += 1
    skip = (int(page) -1) * limit
    return { 'data': db.query(Note).offset(skip).limit(limit).all(), 'total': total}