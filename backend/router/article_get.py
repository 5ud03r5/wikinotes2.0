from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_
from typing import Optional, List
from db.database import get_db
from schemas import ArticleDisplay
from db.models import Article, Tag
from uuid import UUID
router = APIRouter(prefix='/articles', tags=['articles'])

@router.get('/{article_id}')
def get_all_articles(article_id = UUID,  tags = Optional[list], db: Session = Depends(get_db)):
    return db.query(Article).filter(Article.id == article_id).options(joinedload(Article.tags)).first()