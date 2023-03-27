from fastapi import FastAPI # Aqui importamos FastAPI (es una clase)
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
