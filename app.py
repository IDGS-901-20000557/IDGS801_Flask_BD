from flask import Flask 
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from flask import make_response

from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

import forms 

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/", methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.nombre.data,
                       email = create_form.email.data
        )
        # Insert en la BD
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html', form = create_form)

@app.route("/ABCompleto", methods=['GET', 'POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    # Select * from alumnos
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form=create_form, alumnos=alumnos)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        # Select * from alumnos where id==id    
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=alum1.id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        id = create_form.id.data
        # Select * from alumnos where id==id    
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html', form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        # Select * from alumnos where id==id    
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=alum1.id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        id = create_form.id.data
        # Select * from alumnos where id==id    
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('eliminar.html', form=create_form)

@app.route('/resistencias', methods=['GET', 'POST'])
def resistencias():

    #Valores que se devuelven para la tabla, deben ser inicializados
    valorHexBanda1= ""
    valorHexBanda2= ""
    valorHexBanda3=""
    valorHexTolerancia= ""
    valorResistencia=""
    maxValor=""
    minValor=""

    if (request.method == "POST"):
        """ Guardar en el txt """
        seleccionBanda1 = request.form.get('selectPrimer')
        seleccionBanda2 = request.form.get('selectSeg')
        seleccionBandaMulti = request.form.get('selectTer')
        print("pa"*500)
        print(request.form.get('tolerancia'))
        seleccionTolerancia = request.form.get('tolerancia')

        with open('resistencias.txt', 'w') as f:
                f.write(seleccionBanda1+','+seleccionBanda2+','+seleccionBandaMulti+','+seleccionTolerancia)  

        """ Mostrar Tabla """
        archivo = open('resistencias.txt', 'r')
        datos = archivo.readline()

        print(datos)
        array = datos.split(',')
        valorHexBanda1= array[0]
        valorHexBanda2= array[1]
        valorHexBanda3= array[2]
        valorHexTolerancia= array[3]
        
        #Generamos las operaciones
        coloresBanda = {"0": "black", "1": "brown", "2": "red", "3": "orange", "4": "yellow", "5": "green", "6": "blue",
                    "7": "purple", "8": "grey", "9": "white"}
        coloresBandaMultiplicadora = {"1": "black", "10": "brown", "100": "red", "1000": "orange", "10000": "yellow", "100000": "green",
                                  "1000000": "blue", "10000000": "purple", "100000000": "grey", "1000000000": "white"}
        primerNum=""
        segundoNum=""
        multiplicador=""
        #Recorremos el diccionario de datos para verificar nuestro valor de resistencia
        for elemento in coloresBanda:
           if valorHexBanda1==coloresBanda[elemento]:
               primerNum=elemento
           if valorHexBanda2==coloresBanda[elemento]:
               segundoNum=elemento

        #Recorremos el diccionario de datos del multiplicador
        for elemento in coloresBandaMultiplicadora:
           print(elemento, '->', coloresBandaMultiplicadora[elemento])
           if valorHexBanda3==coloresBandaMultiplicadora[elemento]:
               multiplicador=elemento

        numeroTotal=primerNum+segundoNum
        print(multiplicador)
        valorResistencia=int(numeroTotal)*int(multiplicador)
        
        if valorHexTolerancia=="gold":
            maxValor=valorResistencia*1.05
            minValor=valorResistencia-(valorResistencia*.05)
        elif valorHexTolerancia=="silver":
            maxValor=valorResistencia*1.10
            minValor=valorResistencia-(valorResistencia*.10)


        

    response = make_response(render_template('resistencias.html', valorHexBanda1 = valorHexBanda1, valorHexBanda2 = valorHexBanda2, 
                                             valorHexBanda3 = valorHexBanda3, valorHexTolerancia = valorHexTolerancia, valorResistencia = valorResistencia,
                                             maxValor = maxValor, minValor = minValor))
    return response


if __name__ == '__main__':
    # Aplicar la seguridad CSRF al inicializar la aplicación
    csrf.init_app(app)
    # Objeto para la manipulación de la BD
    db.init_app(app)
    # Comprueba si la BD existe y genera un mapeo en automático de las tablas
    with app.app_context():
        db.create_all()
    app.run(port=3000)