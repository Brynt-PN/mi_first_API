#CODIGO COMENTADO DE INTRODUCCIÓN EN LA RAMA INT
from fastapi import FastAPI, Body, Path, Query #PATH nos ayuda a Validar los parametros (Tambien es una Clase (CLASS)). Tambien importamos Query.
from fastapi.responses import HTMLResponse, JSONResponse # Importamos JSONResponse, para devolver las respuestas en formato Json
from pydantic import BaseModel, Field # Importamos BASEMODEL para poder hacer esquemas (Crear clases que ereden caracteristicas de un MODELO BASE)
# FIELD es para hacer validaciones.
from typing import Optional, List # Importamos para poder indicar que hay valores opcionales, LIST es para optener respuestas en formato de Lista

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
    rating: float = Field(ge = 1, le= 10)# Asi como LE determina '>=', GE determina '>='
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


@app.get('/movies',tags=['MOVIES'], response_model = List[Movie]) # Con 'response_model' indicamos el formato de respuesta que queremos y con 'LIST' indicamos que tipo de lista queremos.
def get_movies():
    return JSONResponse(content=movies) # Instauramos JSONResponse y le pasamos como parametro al contenido

@app.get('/movies/{id}', tags=['MOVIES'])
def get_movie(id: int = Path(ge=1,le=2000)) -> Movie: # De esta forma podemos validar el parametro id, usando GE y LE como en ejemplos anteriores.
    # De igual forma que en la ruta anterior podemos definir el tipo de respuesta desde la función con '-> Movie' Solo que aqui no seria una Lista de Peliculas sino solo una. 
    for item in movies:
        if item['id'] == id:
            return JSONResponse(content=item) 
    return JSONResponse(content='ID invalido')

@app.get('/movies/', tags=['MOVIES'], response_model = List[Movie])
def get_movies_by_category(category: str =  Query(min_length = 5, max_length =15 )):# Con QUERY validamos datos de los parametros
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content=data)

@app.post('/movies', tags=['MOVIES'], response_model= dict) # Aqui usamos 'response_model' para indicar que la respuesta es un Diccionario.
def create_movie(movie: Movie): # De la misma forma que indicamos el tipo de parametro podemos pasarle una clase como tipo de parametro de tal forma que 'movie: Movie' indica que el parametro movie es de la clase Movie. (Es como instaurarlo)

    movies.append(movie) # Agregamos a la lista 'movies' el objeto 'movie', aqui solo pasamos ese parametro y nos ahorramos colocar todos las caracteristicas.
    return JSONResponse(content= {'message':'Se ha registrado la pelicula'}) # Asi podemos usar JSONResponse para dar un mensaje por pantalla.

@app.put('/movies/{id}', tags=['MOVIES'], response_model= dict)
def update_movies(id: int, movie: Movie): # Nuevamente instauramos el objeto 'movie' de la clase 'Movie', dejamos el parametro ID por que ese si lo necesitamos como parametro de filtro
    for item in movies: 
        if item['id'] == id: 
            item['title'] = movie.title # Con esta sintaxis 'movie.title' accedemos a la caraccteristica 'title' del objeto 'movie'.
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










