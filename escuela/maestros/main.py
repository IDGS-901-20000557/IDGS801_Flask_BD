from db import get_connection


def insertarMaestro(nombre,apellidom,apellidop,email):
    try:
                connection=get_connection()
                with connection.cursor() as curso:
                    curso.execute('call agrega_maestro(%s,%s,%s,%s)',(nombre,apellidom,apellidop,email))
                connection.commit()    
                connection.close()     
               
    except Exception as ex:
                print(ex) 

def eliminarMaestro(idMaestro):
    try:
          
            connection=get_connection()
            with connection.cursor() as curso:
                curso.execute('call eliminar_maestro(%s)',(idMaestro,))
            connection.commit()    
            connection.close()
        
    except Exception as ex:
            print(ex) 

def consultarMaestro(idMaestro):
    try:
            connection=get_connection()
            with connection.cursor() as curso:
                curso.execute('call consulta_maestro(%s)',(idMaestro,))
                resultset=curso.fetchone()
                for row in resultset:
                    print(row)
                id=resultset[0]
                nombre=resultset[1]
                apellidop=resultset[3]
                apellidom=resultset[2]
                email=resultset[4]
            connection.close()
            return (id, nombre, apellidop,apellidom,email)
    except Exception as ex:
            print(ex) 

def modificarMaestro(idMaestro,nombre,apellidom,apellidop,email):
    try:
            connection=get_connection()
            with connection.cursor() as curso:
                curso.execute('call actualizar_maestro(%s,%s,%s,%s,%s)',(idMaestro,nombre,apellidom,apellidop,email))
            connection.commit()    
            connection.close()
           
    except Exception as ex:
            print(ex) 


def consultarMaestros():
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('call consulta_maestros()')
            resultset=curso.fetchall()
            for row in resultset:
                print(row)
        connection.close()
        return resultset
    except Exception as ex:
        print(ex) 