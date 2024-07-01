from flask import Flask
from app.database import init_app
from app.views import *
from flask_cors import CORS

#crear una instancia de flask
app = Flask(__name__)

init_app(app) 
#permitir solicitudes desde cualquier origen
CORS(app)
#asociacion de rutas con vistas
app.route('/usuarios',methods=['GET'])(get_all_usuarios)
app.route('/usuarios',methods=['POST'])(create_usuario)
app.route('/usuarios/<int:user_id>',methods=['PUT'])(update_usuario)
app.route('/usuarios/<int:user_id>',methods=['DELETE'])(delete_usuario)
app.route('/pictures',methods=['GET'])(get_all_pictures)

if __name__ == '__main__':
     app.run(debug=True, host="0.0.0.0") 