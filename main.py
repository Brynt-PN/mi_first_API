from fastapi import FastAPI, Body 
from fastapi.responses import HTMLResponse 

app = FastAPI() 
app.title = 'Mi First API con FastAPI' 
app.version = '0.0.1' 

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
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(),category: str = Body()): 
    movies.append(
        {
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category    
    } 
    ) 
    return movies

@app.put('/movies/{id}', tags=['MOVIES'])
def update_movies(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(),category: str = Body()):
    for item in movies: 
        if item['id'] == id: 
            item['title'] = title
            item['overview'] = overview
            item['year'] = year
            item['rating'] = rating
            item['category'] = category
            return movies
    return 'ID invalido'

@app.delete('/movie{id}', tags=['MOVIES'])
def delete_movie(id: int):
    for item in movies: 
        if item['id'] == id: #
            movies.remove(item)
            return movies
    return 'ID invalido' 










