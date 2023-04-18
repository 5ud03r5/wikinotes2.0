from fastapi import FastAPI
from router import articles_get, notes_get, articles_post, notes_post, articles_delete, tags_get, article_get
from fastapi.middleware.cors import CORSMiddleware
from db import models
from db.database import engine, SessionLocal
origins = "*"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(articles_get.router)
app.include_router(articles_post.router)
app.include_router(notes_get.router)
app.include_router(notes_post.router)
app.include_router(articles_delete.router)
app.include_router(tags_get.router)
app.include_router(article_get.router)
models.Base.metadata.create_all(bind=engine)