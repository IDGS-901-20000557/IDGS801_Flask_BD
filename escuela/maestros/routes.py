from flask import redirect, render_template, Blueprint
from flask import request
from flask import url_for
import forms 
from .main import insertarMaestro, eliminarMaestro, consultarMaestro, modificarMaestro,consultarMaestros

from flask import Blueprint, render_template


maestros = Blueprint('maestros', __name__)

@maestros.route("/agregarMaestro", methods=["GET", "POST"])
def insertarMaestroVista():
    create_form=forms.UserFormMaestro(request.form)
    if request.method=='POST':
         insertarMaestro(create_form.nombre.data,create_form.apellidom.data,create_form.apellidop.data, create_form.email.data)
         return redirect(url_for('maestros.ABCompletoMaestros'))
    return render_template('agregarMaestro.html', form=create_form)


@maestros.route("/eliminarMaestro", methods=['GET', 'POST'])
def eliminarMaestroVista():
    create_form=forms.UserFormMaestro(request.form)

    if request.method=='GET':
        (idmaestro, nombre, apellidop,apellidom,email) = consultarMaestro(request.args.get('id'))
        create_form.id.data=idmaestro
        create_form.nombre.data=nombre
        create_form.apellidop.data=apellidop
        create_form.apellidom.data=apellidom
        create_form.email.data=email
    if request.method=='POST':
        eliminarMaestro(create_form.id.data)
        return redirect(url_for('maestros.ABCompletoMaestros'))
        
    print( request.form.get("id"))
    print(request.args.get('id'))
    print(create_form.id.data)
    print(create_form.nombre.data)
    return render_template('eliminarMaestro.html', form=create_form)


@maestros.route("/modificarMaestro", methods=['GET', 'POST'])
def modificarMaestroVista():
    create_form=forms.UserFormMaestro(request.form)
    if request.method=='GET':
        (id, nombre, apellidop,apellidom,email) =consultarMaestro(request.args.get('id'))
        create_form.id.data=id
        create_form.nombre.data=nombre
        create_form.apellidop.data=apellidop
        create_form.apellidom.data=apellidom
        create_form.email.data=email
    if request.method=='POST':
        modificarMaestro(create_form.id.data,create_form.nombre.data,create_form.apellidom.data,create_form.apellidop.data, create_form.email.data)
        return redirect(url_for('maestros.ABCompletoMaestros'))
       
    return render_template('modificarMaestro.html', form=create_form)


@maestros.route("/ABCompletoMaestros", methods=['GET', 'POST'])
def ABCompletoMaestros():
    resultset=consultarMaestros()
    create_form=forms.UserFormMaestro(request.form)
    return render_template('ABCompletoMaestros.html', form=create_form, maestros=resultset)


