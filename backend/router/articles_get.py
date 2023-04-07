from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from typing import Optional, List
from db.database import get_db
from schemas import ArticleDisplay
from db.models import Article, Tag, articles_tags

router = APIRouter(prefix='/articles', tags=['articles'])

@router.get('/')
def get_all_articles(limit: Optional[int] = 3, page = 1, db: Session = Depends(get_db)):
    
    total_articles = db.query(Article).count()
    total = total_articles // limit
    if total_articles % limit > 0:
        total += 1
    skip = (int(page) -1) * limit
    
    #db.query(Article).join(Article.tags)
    return { 'data': db.query(Article).options(joinedload(Article.tags)).offset(skip).limit(limit).all(), 'total': total}