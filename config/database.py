import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
sqlite="../database.sqlite"
base_dir=os.path.dirname(os.path.realpath(__file__))

database_url=f"sqlite:///{os.path.join(base_dir, sqlite)}" 

#representa el motor de la base de datos"
engine=create_engine(database_url,echo=True)
Session= sessionmaker(bind=engine)

Base1= declarative_base()