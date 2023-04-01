# En este archivo crearemos la función generadora del token de validación para la autenticación de la cuenta.
from jwt import encode # Importamos de JWT la clase ENCODE 

def create_token(data: dict): # Definimos la función para crear el token y le pasamos un parametro 'DATA' que contrendra todo la info necesaria para crear el token, y definimos que tendra formato de DICCIONARIO.
    token: str = encode(payload=data, key='1998', algorithm='HS256') # Aqui defenimos una variable 'TOKEN' indicamos que es de tipo 'STRING' y la instauramos con la Clase 'ENCODE' y le pasamos los parametros 'pyload' es el contenido que queremos guardar dentro del token 'DATA', 'key' que es una cadena secreta utilizada para firmar el token (debe ser un string y servira para desifrar el token), 'algorithm' que es el algoritmo de cifrado utilizado para firmar el token. En este caso, se utiliza el algoritmo "HS256" (que lo sugiere directamente el programa)
    return token # Retornamos el valor de 'TOKEN'