from fastapi import FastAPI, Body # Aqui importamos FastAPI (es una clase) y Tambien BODY nos ayuda a definir que variables que son parte de una solicitud POST
from fastapi.responses import HTMLResponse # Importamos para poder devolver un HTML

app = FastAPI() # Instanciamos (Crear un OBJ a partir de una CLASS), que sera nuestra APP
# OBS: para lansar el servidor con UVICOR el comando es 'uvicorn main:app' para que se actualice automaticamente usar al final '--reload'
# Para asignar un puerto determinado pordemos usar '--port 5000', podemos colocar cualquier puerto que querramos, paraojeto del curso usamos el '5000'
# Para poder ejecutarlo desde un dispositivo movil que este en nuestra red usamos '--host 0.0.0.0' con eso estara disponible para todos los dispositivos en la red.

app.title = 'Mi First API con FastAPI' # Con esto colocamos Titulo a la documentación de la API
# Para leer la documentación de la API en el navegador al final del link agregamos un '/docs'

app.version = '0.0.1' # Con esto colocamos la version a la documentación de la API 

# A continuación definimos una RUTA
@app.get('/', tags=['HOME']) # Con la etiqueta TAGS podemos agrupar distintas rutas, tambien se ve reflejado en la documentación.
def message():
    return HTMLResponse('<h1>HOLA MUNDO</h1>')

# Definimos una lista de diccionarios que contiene información sobre películas
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

# Definimos una ruta para la API que devuelve toda la lista de películas
@app.get('/movies',tags=['MOVIES'])
def get_movies():
    return movies

# Definimos una ruta para la API que recibe un ID de película y devuelve la película correspondiente
@app.get('/movies/{id}', tags=['MOVIES'])
def get_movie(id: int): # Indicamos que el ID debe ser un INT (Entero)
    for item in movies:
        if item['id'] == id:# Verificamos si el valor de la clave 'id' coincide con el valor del parámetro 'id' proporcionado
            return item # Retornamos el ITEM que seria el dicciónario correspondiente
    return 'ID invalido'

# Definimos una ruta para la API que recibe una categoría de película y devuelve una lista de todas las películas en esa categoría
@app.get('/movies/', tags=['MOVIES'])
def get_movies_by_category(category: str):
    # Usamos una lista de comprensión para iterar sobre cada elemento de la lista de películas y devolver solo aquellos cuya categoría coincida con la proporcionada
    return [item for item in movies if item['category'] == category]

# Definimos una ruta para el metodo POST, para poder agregar una registro a la lista
@app.post('/movies', tags=['MOVIES'])
# Aqui los parametros deben venir con la petición como parte del cuerpo que se agregaran al registro
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(),category: str = Body()): # Usamos BODY para definir que parametros son parte del cuerpo de la solicitud POST
    movies.append(
        {
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category    
    } 
    ) # Aqui añadimos a la lista el nuevo registro utilizando los parametros
    return movies

# Definimos una ruta para el metodo PUT, para actualizar un registro de nuestra lista
@app.put('/movies/{id}', tags=['MOVIES'])
# A diferencia del anterior aqui para identificar el registro a actualizar usamos el paraetro ID, por eso si se tiene como parametro requerido fuera del cuerpo de la solicitud.
def update_movies(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(),category: str = Body()):
    for item in movies: # Iteramos la lista hasta encontrar el registro correspondiente y actualizamos sis valores
        if item['id'] == id: # OBS: '==' para comparativa '=' para asignar valor
            item['title'] = title
            item['overview'] = overview
            item['year'] = year
            item['rating'] = rating
            item['category'] = category
            return movies
    return 'ID invalido'

# Definimos una ruta para el método DELETE que elimina un registro de nuestra lista en función de su ID
@app.delete('/movie{id}', tags=['MOVIES'])
def delete_movie(id: int):
    for item in movies: # Iteramos sobre la lista de películas para encontrar el registro correspondiente
        if item['id'] == id: # Si encontramos el registro, lo eliminamos de la lista de películas y devolvemos la lista actualizada
            movies.remove(item)
            return movies
    return 'ID invalido' # Si el ID proporcionado no coincide con ningún registro en la lista, devolvemos un mensaje de error

#ANOTACIONES DE INTRO HASTA ESTE PUNTO, CONTINUAMOS EN LA RAMA 'MASTER' CON ANOTACIONES DE CERO










