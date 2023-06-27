from fastapi.security import HTTPBearer
from fastapi import Request,HTTPException
from utils.jwt_manager import token,v_token

class jwtBearer(HTTPBearer):
   async def __call__(self, request: Request):
      auth=await super().__call__(request)
      data=v_token(auth.credentials)
      if data["email"]!="admin@gmail.com":
         raise HTTPException(status_code=403,detail="credentials invalid")