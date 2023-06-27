from fastapi import FastAPI
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel
from sqlalchemy.orm.session import sessionmaker
from starlette.requests import Request
from config.database import Session,engine, Base1
from middleware.error_handler import error_handler
from routers.login_user import user_router

from routers.movie import movie_router


Base1.metadata.create_all(bind=engine)


app= FastAPI()
app.title="APP #1"
app.version="1.0.1"
app.add_middleware(error_handler)
app.include_router(movie_router)
app.include_router(user_router)
movies=[{'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'},
        {'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'}]

@app.get("/",tags=["home"],status_code=200)

def message():
    return HTMLResponse("<h1> Hola </h1>")


   

  
