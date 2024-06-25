from flask import Flask
from app.database import init_app
from app.views import get_all_usuarios

#craer una instancia de flask
app = Flask(__name__)

init_app(app) 

#asociacion de rutas con vistas
app.route('/usuarios',methods=['GET'])(get_all_usuarios)

if __name__ == '__main__':
     app.run(debug=True) 