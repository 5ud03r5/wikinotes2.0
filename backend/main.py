from fastapi import FastAPI
from router import articles_get, notes_get
from fastapi.middleware.cors import CORSMiddleware

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
app.include_router(notes_get.router)