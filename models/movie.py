from config.database import Base1
from sqlalchemy import Column,Integer,FLOAT,String

class movie(Base1):
    __tablename__="movies"

    id=Column(Integer,primary_key=True)
    title=Column(String)
    overview=Column(String)
    year=Column(Integer)
    rating=Column(FLOAT)
    category=Column(String)