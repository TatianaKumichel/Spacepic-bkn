from flask import jsonify, request
from app.models import Usuario


def index():
    response = {'message':'Hola mundo API FLASK 🐍'}#logica de negocio, para guardar en la base de datos o
                #lo que necesitemos hacer
    return jsonify(response) 
#funcion que busca el listado de usuarios
def get_all_usuarios():
    usuarios = Usuario.get_all()
    list_usuarios = [usuario.serialize()for usuario in usuarios] #recorre el resultado de la linea anterior y convierte el estado a un diccionario
    return jsonify(list_usuarios)

def create_usuario():
    data = request.json #request trae los datos de formato json y los convierte a diccionario de python
    #agregar una logica de validacion de datos 
    new_usuario = Usuario(None, data['nombre'], data['email'])
    new_usuario.save()
    return jsonify({'message':'Usuario creado con exito'}), 201

def update_usuario():
    pass

def delete_usuario():
    pass