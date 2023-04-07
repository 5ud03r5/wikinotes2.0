from db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, Text, DateTime, Table
from sqlalchemy.orm import relationship


articles_tags = Table('articles_tags', Base.metadata,
    Column('article_id', ForeignKey('article.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(UUID, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    created = Column(DateTime)

class Article(Base):
    __tablename__ = 'article'
    id = Column(UUID, primary_key=True, index=True)
    title = Column(String)
    text = Column(Text)
    created = Column(DateTime)
    tags = relationship("Tag",
                    secondary=articles_tags)

class Note(Base):
    __tablename__ = 'note'
    id = Column(UUID, primary_key=True, index=True)
    text = Column(Text)
    created = Column(DateTime)

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    created = Column(DateTime)