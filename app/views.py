from flask import jsonify

def index():
    response = {'message':'Hola mundo API FLASK'}
    return jsonify(response)
                   
def saludar():
    response = {'message': 'Hola estoy SALUDANDO'}                 
    return jsonify(response)
