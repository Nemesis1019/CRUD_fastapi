from models.movie import movie as movieModel
from schemas.movie import movie 
class movie_service():
    def __init__(self,db)->None:
        self.db=db
        
    def get_movies(self):
        result=self.db.query(movieModel).all()
        return result
    
    def get_movie(self,id):
        result=self.db.query(movieModel).filter(movieModel.id==id).first()
        return result
    
    def filter_cat(self,cat):
        result=self.db.query(movieModel).filter(movieModel.category==cat).all()
        return result
    def create_movie(self, Movie:movie):
        new_movie=movieModel(**Movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return 
    def update_movie(self,id:int,data:movie):
        movie=self.db.query(movieModel).filter(movieModel.id==id).first()
        movie.title=data.title
        movie.overview=data.overview
        movie.rating=data.rating
        movie.year=data.year
        movie.category=data.category
        self.db.commit()
        return
    def delete_movie(self,id):
        result=self.db.query(movieModel).filter(movieModel.id==id).first()
        self.db.delete(result)
        self.db.commit()
        return