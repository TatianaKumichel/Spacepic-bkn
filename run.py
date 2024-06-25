from flask import Flask
from app.views import *

app = Flask(__name__)

app.route('/helloworld',methods=['GET'])(index)
app.route('/saludar',methods=['GET'])(saludar)

if __name__=='__main__':
    app.run(debug=True)
