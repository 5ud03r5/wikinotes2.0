from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_
from typing import Optional, List
from db.database import get_db
from schemas import ArticleDisplay
from db.models import Article, Tag, articles_tags

router = APIRouter(prefix='/articles', tags=['articles'])

@router.get('/')
def get_all_articles(limit: Optional[int] = 3, page = 1, tags = Optional[list], search = None, db: Session = Depends(get_db)):
       
    query = db.query(Article).options(joinedload(Article.tags))
    if tags and search:
        tags = tags.split(',')    
        for tag in tags:
            query = query.filter(Article.tags.any(Tag.id == tag))
        query = query.filter(and_(*(Article.tags.any(Tag.id == tag) for tag in tags))).filter(Article.text.contains(search))

    elif search:  
        query = query.filter(Article.text.contains(search))
    elif tags:   
        tags = tags.split(',')    
        for tag in tags:
            query = query.filter(Article.tags.any(Tag.id == tag))
        query = query.filter(and_(*(Article.tags.any(Tag.id == tag) for tag in tags)))

    skip = (int(page) -1) * limit
    if skip < 0:
        skip = 3
    total_articles = query.count()
    total = total_articles // limit
    if total_articles % limit > 0:
        total += 1
    print(total)
    return { 'data': query.offset(skip).limit(limit).all(), 'total': total}