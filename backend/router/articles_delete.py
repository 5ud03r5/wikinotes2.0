from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Optional, List

from db.database import get_db
from schemas import ArticleCreate
from db.models import Article, Tag
from datetime import datetime
from uuid import uuid4, UUID
router = APIRouter(prefix='/articles', tags=['articles'])

@router.delete('/{article_id}')
def create_article(article_id: UUID, db: Session = Depends(get_db)):
    item = db.query(Article).filter(Article.id == article_id).first()
    if item == None:
        return status.HTTP_404_NOT_FOUND
    db.delete(item)
    db.commit()
    return status.HTTP_200_OK