import os
import mysql.connector
from flask import g
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'), 
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT',3306)
}
#funcion para obtener la conexion a la base de datos
def get_db():
    #si db no esta en el contexto global de flask g
    if 'db' not in g:
        #crear una nueva conexion a la base de datos y guardar
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    #retornar la conexion a la base datos
    return g.db

#funcion para cerrar la conexion a la base de datos

def close_db(e=None):
    #extraer la conexion a la base de datos yn eliminarla
    db = g.pop('db',None)
    #si la conexion existe cerraqrla
    if db is not None:
        db.close()
        
        
#funcion para inicializar la aplicacion con el manejo de la base de datos
def init_app(app):
    #registrar 'close_db' para que se ejecute al final del contexto de la aplicacion
    app.teardown_appcontext(close_db)
    