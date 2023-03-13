
from models import db
from models import Alumnos

def insertarAlumno(nombre, apellidos, email):
    alum=Alumnos(nombre=nombre, apellidos=apellidos, email=email)
    db.session.add(alum)
    db.session.commit()

def consultarAlumnos():
    #select * from alumnos
    alumnos=Alumnos.query.all()
    return alumnos

def consultarAlumno(idAlumno):
        #select * from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==idAlumno).first()
        return  alum1

def modificarAlumno(idAlumno,nombre,apellidos,email):
        #select * from alumnos where id==id
        alum=db.session.query(Alumnos).filter(Alumnos.id==idAlumno).first()
        alum.nombre=nombre
        alum.apellidos=apellidos
        alum.email=email
        db.session.add(alum)
        db.session.commit()

def eliminarAlumno(idAlumno):
        #select * from alumnos where id==id
        alum=db.session.query(Alumnos).filter(Alumnos.id==idAlumno).first()
        db.session.delete(alum)
        db.session.commit()
        