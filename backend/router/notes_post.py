from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional, List
from db.database import get_db
from schemas import NoteCreate
from db.models import Note
from datetime import datetime
from uuid import uuid4
router = APIRouter(prefix='/notes', tags=['notes'])

@router.post('/')
def create_note(request: NoteCreate, db: Session = Depends(get_db)):
    new_note = Note(
        id = uuid4(),
        text = request.text,
        created = datetime.now()
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note