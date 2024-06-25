from flask import jsonify
from app.models import Usuario


def index():
    response = {'message':'Hola mundo API FLASK 🐍'}#logica de negocio, para guardar en la base de datos o
                #lo que necesitemos hacer
    return jsonify(response) 
#funcion que busca el listado de usuarios
def get_all_usuarios():
    usuarios = Usuario.get_all()
    list_usuarios = [usuario.serialize()for usuario in usuarios]
    return jsonify(list_usuarios)

def create_usuario():
    pass

def update_usuario():
    pass

def delete_usuario():
    pass