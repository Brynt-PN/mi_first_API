#CODIGO COMENTADO DE INTRODUCCIÓN EN LA RAMA INT
#CODIGO COMENTADO DE INTERMEDIO EN LA RAMA MED
from fastapi import FastAPI, Body, Path, Query 
from fastapi.responses import HTMLResponse, JSONResponse 
from pydantic import BaseModel, Field 
from typing import Optional, List 

app = FastAPI() 
app.title = 'Mi First API con FastAPI' 
app.version = '0.0.1' 


class Movie(BaseModel):
    id: Optional[int] = None 
    title: str = Field(default= 'Mi Pelicula', min_length= 5, max_length= 15)
    overview: str = Field(min_length= 15, max_length= 50)
    year: int = Field(le= 2024) 
    rating: float = Field(ge = 1, le= 10)
    category: str 

    class Config:
        schema_extra = {
            'example': {
                'id' : 0,
                'title':'Mi pelicula',
                'overview':'Descripcíon de la Pelicula',
                'year': 2022,
                'rating' : 5.5,
                'category' : 'Acción'
            }
        }



@app.get('/', tags=['HOME']) 
def message():
    return HTMLResponse('<h1>HOLA MUNDO</h1>')

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Duro de Matar',
        'overview': "Un policia de NY llega al Nacatomi Plaza para ver a su ex esposa e hijos por navidad y termina en un secuestro terrorista ...",
        'year': '1988',
        'rating': 9.4,
        'category': 'Acción'    
    } 
]


@app.get('/movies',tags=['MOVIES'], response_model = List[Movie]) 
def get_movies():
    return JSONResponse(content=movies) 

@app.get('/movies/{id}', tags=['MOVIES'])
def get_movie(id: int = Path(ge=1,le=2000)) -> Movie: 
    for item in movies:
        if item['id'] == id:
            return JSONResponse(content=item) 
    return JSONResponse(content='ID invalido')

@app.get('/movies/', tags=['MOVIES'], response_model = List[Movie])
def get_movies_by_category(category: str =  Query(min_length = 5, max_length =15 )):
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content=data)

@app.post('/movies', tags=['MOVIES'], response_model= dict) 
def create_movie(movie: Movie): 

    movies.append(movie) 
    return JSONResponse(content= {'message':'Se ha registrado la pelicula'})

@app.put('/movies/{id}', tags=['MOVIES'], response_model= dict)
def update_movies(id: int, movie: Movie): 
    for item in movies: 
        if item['id'] == id: 
            item['title'] = movie.title 
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category 
            return JSONResponse(content= {'message':'Se ha modificado la pelicula'})
    return 'ID invalido'

@app.delete('/movie{id}', tags=['MOVIES'], response_model= dict)
def delete_movie(id: int):
    for item in movies: 
        if item['id'] == id: 
            movies.remove(item)
            return JSONResponse(content= {'message':'Se ha eliminado la pelicula'})
    return 'ID invalido' 










