#CODIGO COMENTADO DE INTRODUCCIÓN EN LA RAMA INT
from fastapi import FastAPI, Body 
from fastapi.responses import HTMLResponse 
from pydantic import BaseModel, Field # Importamos BASEMODEL para poder hacer esquemas (Crear clases que ereden caracteristicas de un MODELO BASE)
# FIELD es para hacer validaciones.
from typing import Optional # Importamos para poder indicar que hay valores opcionales

app = FastAPI() 
app.title = 'Mi First API con FastAPI' 
app.version = '0.0.1' 

# Creamos una clase para los Objetos MOVIE, que ereda de BASEMODEL (Modelo Base)
class Movie(BaseModel):# Luego indicamos las caracteristicas de esta clase (Asi ahorramos codigo mas adelante en POST Y DELET)
    id: Optional[int] = None # Con OPTIONAL indicamos que el ID es un valor que puede ser Opcional, con '[int]' indicamos su valor entero y con '= None' decimos que su valor predeterminado es NULO
    title: str = Field(default= 'Mi Pelicula', min_length= 5, max_length= 15) # Con 'Field' podemos pasar validaciones como datos, por ejemplo, colocar un dato por defecto y tambuen un minimo y máximo de caracteres.
    # OBS: Field es una Clase (CLASS) 

    overview: str = Field(min_length= 15, max_length= 50)
    year: int = Field(le= 2024) #Para el caso de definir un rango en valores INT (Enteros) usamos 'LE'
    rating: float = Field(le= 10)
    category: str 

    class Config: # Creamos una Clase con un esquema extra en la cual colocamos los valores predeterminados de lso parametros de la clase anterior, esto remplaza el varo por defencto que colocamos en FIELD.
        #OBS: esto invalida los default de FIELD
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
def create_movie(movie: Movie): # De la misma forma que indicamos el tipo de parametro podemos pasarle una clase como tipo de parametro de tal forma que 'movie: Movie' indica que el parametro movie es de la clase Movie. (Es como instaurarlo)

    movies.append(movie) # Agregamos a la lista 'movies' el objeto 'movie', aqui solo pasamos ese parametro y nos ahorramos colocar todos las caracteristicas.
    return movies

@app.put('/movies/{id}', tags=['MOVIES'])
def update_movies(id: int, movie: Movie): # Nuevamente instauramos el objeto 'movie' de la clase 'Movie', dejamos el parametro ID por que ese si lo necesitamos como parametro de filtro
    for item in movies: 
        if item['id'] == id: 
            item['title'] = movie.title # Con esta sintaxis 'movie.title' accedemos a la caraccteristica 'title' del objeto 'movie'.
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










