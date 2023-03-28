#CODIGO COMENTADO DE INTRODUCCIÓN EN LA RAMA INT
from fastapi import FastAPI, Body 
from fastapi.responses import HTMLResponse 
from pydantic import BaseModel # Importamos BASEMODEL para poder hacer esquemas (Crear clases que ereden caracteristicas de un MODELO BASE)
from typing import Optional # Importamos para poder indicar que hay valores opcionales

app = FastAPI() 
app.title = 'Mi First API con FastAPI' 
app.version = '0.0.1' 

# Creamos una clase para los Objetos MOVIE, que ereda de BASEMODEL (Modelo Base)
class Movie(BaseModel):# Luego indicamos las caracteristicas de esta clase (Asi ahorramos codigo mas adelante en POST Y DELET)
    id: Optional[int] = None # Con OPTIONAL indicamos que el ID es un valor que puede ser Opcional, con '[int]' indicamos su valor entero y con '= None' decimos que su valor predeterminado es NULO
    title: str
    overview: str
    year: int
    rating: float
    category: str

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


@app.get('/movies',tags=['MOVIES'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['MOVIES'])
def get_movie(id: int): 
    for item in movies:
        if item['id'] == id:
            return item 
    return 'ID invalido'

@app.get('/movies/', tags=['MOVIES'])
def get_movies_by_category(category: str):
    return [item for item in movies if item['category'] == category]

@app.post('/movies', tags=['MOVIES'])
def create_movie(movie: Movie): # Declaramos que queremos un objeto 'movie' y que es de la clase 'Movie'
    movies.append(movie) # Aqui indicamos que añada 'movie' directamente en lugar de pasar todos los parametros, ya que al ser un objeto los tiene como caracteristicas.
    return movies

@app.put('/movies/{id}', tags=['MOVIES'])
def update_movies(id: int, movie: Movie): # Nuevamente instauramos el objeto 'movie' de la clase 'Movie', dejamos el parametro ID por que ese si lo necesitamos como parametro de filtro
    for item in movies: 
        if item['id'] == id: 
            item['title'] = movie.title # Con esta sintaxis 'movie.title' indicamos que tome el valor de la caracteristica TITLE del objeto 'movie'
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category 
            return movies
    return 'ID invalido'

@app.delete('/movie{id}', tags=['MOVIES'])
def delete_movie(id: int):
    for item in movies: 
        if item['id'] == id: 
            movies.remove(item)
            return movies
    return 'ID invalido' 










