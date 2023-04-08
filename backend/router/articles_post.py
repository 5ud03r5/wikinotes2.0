from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional, List
from db.database import get_db
from schemas import ArticleCreate
from db.models import Article, Tag
from datetime import datetime
from uuid import uuid4
router = APIRouter(prefix='/articles', tags=['articles'])

@router.post('/')
def create_article(request: ArticleCreate, db: Session = Depends(get_db)):
    print(request.tags)
    tags = []
    for tag in request.tags:
        db_tag = db.query(Tag).filter(Tag.name == tag['name']).first()     
        if db_tag is None:
            new_tag = Tag(id = uuid4(), name=tag['name'])
            tags.append(new_tag)        
        else:
            tags.append(db_tag)        
    new_article = Article(
        id = uuid4(),
        title = request.title,
        text = request.text,
        tags = tags,
        created = datetime.now()
    )
    

    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article