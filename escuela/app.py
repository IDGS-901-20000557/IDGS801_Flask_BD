from flask import Flask,redirect, render_template
from flask import request
from flask import url_for
import forms 

from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()
from maestros.routes import maestros
from alumnos.routes import alumnos
app.config['DEBUG']=True





#Rutas
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')



app.register_blueprint(maestros)
app.register_blueprint(alumnos)






if __name__== '__main__':
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)