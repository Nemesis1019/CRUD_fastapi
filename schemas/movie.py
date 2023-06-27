from pydantic import BaseModel, Field
from typing import Optional,List
class movie(BaseModel):
   id:Optional[int]=None
   title:str=Field(default="Mi pelicula",min_length=5,max_length=15)
   overview:str=Field(default="Descripción",min_length=5,max_length=50)
   year:int=Field(default=2022,le=2022)
   rating:float=Field(ge=1,le=10)
   category:str
   