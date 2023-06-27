from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional,List
from fastapi.responses import HTMLResponse,JSONResponse
from utils.jwt_manager import  token,v_token
from schemas.user import User

user_router=APIRouter()



@user_router.post("/login",tags=["auth"])
def login(user:User):
   if user.email=="admin@gmail.com" and user.password=="admin":
      tokenn:str=token(user.dict())
      return JSONResponse(status_code=200,content=tokenn)
