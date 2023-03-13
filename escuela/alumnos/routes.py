from flask import redirect, render_template, Blueprint
from flask import request
from flask import url_for
import forms 
from .main import insertarAlumno, eliminarAlumno, consultarAlumno, modificarAlumno,consultarAlumnos

from flask import Blueprint, render_template



alumnos = Blueprint('alumnos', __name__)

@alumnos.route("/agregarAlumno", methods=["GET", "POST"])
def agregarAlumnoVista():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        insertarAlumno(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data,
                     email=create_form.email.data)
        return redirect(url_for('alumnos.ABCompletoAlumno'))

    return render_template('index.html', form=create_form)

@alumnos.route("/ABCompletoAlumno", methods=['GET', 'POST'])
def ABCompletoAlumno():
    create_form=forms.UserForm(request.form)
    alumnos=consultarAlumnos()
    return render_template('ABCompleto.html', form=create_form, alumnos=alumnos)


@alumnos.route("/modificarAlumno", methods=['GET', 'POST'])
def modificarAlumnoVista():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        alum1=consultarAlumno(request.args.get('id'))
        create_form.id.data=alum1.id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        modificarAlumno(create_form.id.data,create_form.nombre.data,create_form.apellidos.data,create_form.email.data)
       
        return redirect(url_for('alumnos.ABCompletoAlumno'))
    return render_template('modificar.html', form=create_form)

@alumnos.route("/eliminarAlumno", methods=['GET', 'POST'])
def eliminarAlumnoVista():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        alum1=consultarAlumno(request.args.get('id'))
        create_form.id.data=alum1.id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email
    if request.method=='POST':
        eliminarAlumno(create_form.id.data)
        return redirect(url_for('alumnos.ABCompletoAlumno'))
    return render_template('eliminar.html', form=create_form)
