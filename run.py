from flask import Flask
from app.database import init_app
from app.views import *

#crear una instancia de flask
app = Flask(__name__)

init_app(app) 

#asociacion de rutas con vistas
app.route('/usuarios',methods=['GET'])(get_all_usuarios)
app.route('/usuarios',methods=['POST'])(create_usuario)
app.route('/usuarios',methods=['PUT'])(update_usuario)
app.route('/usuarios',methods=['DELETE'])(delete_usuario)
app.route('/pictures',methods=['GET'])(get_all_pictures)

if __name__ == '__main__':
     app.run(debug=True) 