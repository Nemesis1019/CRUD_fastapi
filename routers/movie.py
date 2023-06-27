from fastapi import APIRouter
from fastapi import Path,Query,Depends
from fastapi.responses import JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Optional,List
from sqlalchemy.orm.session import sessionmaker
from starlette.requests import Request
from config.database import Session
from models.movie import movie as MovieModel
from fastapi.encoders import jsonable_encoder
from utils.jwt_manager import  token,v_token
from middleware.jwt_bearer import jwtBearer
from services.movie import movie_service
from schemas.movie import movie
from schemas.user import User
movie_router= APIRouter()

@movie_router.get("/movies",tags=["movies"], response_model=List[movie],status_code=200)

def getmovies()->List[movie]:
    db=Session()
    result=movie_service(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result))

@movie_router.get("/movies/{id}",tags=["movies"],response_model=movie)
def get_function(id:int=Path(ge=1,le=2000))->movie:   
   db=Session()
   result=movie_service(db).get_movie(id)
   if not result:
      return JSONResponse(status_code=200, content={"mesage":"efe veneco"})
   return JSONResponse(content=jsonable_encoder(result))

@movie_router.get("/movies/",tags=["movies"],response_model=movie)

def get_movies(category:str=Query(min_length=5,max_length=20))->movie:
   db=Session()
   result=movie_service(db).filter_cat(category)
   return JSONResponse(content=jsonable_encoder(result))

@movie_router.post("/movies",tags=["movies"],response_model=dict,status_code=201)
def post(movie:movie)->dict:
    db=Session()
    movie_service(db).create_movie(movie)
    return JSONResponse(status_code=201,content={"message":"se registro la peli"})

@movie_router.put("/movies/{id}",tags=["movies"],response_model=dict)
def update(id:int,movie:movie)->dict:
    db=Session()
    result = movie_service(db).get_movie(id)
    if not result:
       return JSONResponse(status_code=200, content={"mesage":"efe veneco"})
    movie_service(db).update_movie(id, movie)
    return JSONResponse(content={"message":"se modifico la peli"})

@movie_router.delete("/movies/{id}",tags=["movies"],response_model=dict,status_code=200)

def delete(id:int)->dict:
    db=Session()
    result=db.query(MovieModel).filter(MovieModel.id==id).first()
    if not result:
       return JSONResponse(status_code=200, content={"mesage":"efe veneco"})
    movie_service(db).delete_movie(id)
      
    return JSONResponse(content={"message":"se borró la peli"})  