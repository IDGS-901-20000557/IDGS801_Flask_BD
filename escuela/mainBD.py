
from db import get_connection

""" try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('call consulta_alumnos()')
        resultset=curso.fetchall()
        for row in resultset:
            print(row)
    connection.close()
    
except Exception as ex:
    print('error') """

""" try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('call consulta_alumno(%s)',(14,))
        resultset=curso.fetchone()
        for row in resultset:
            print(row)
    connection.close()
    
except Exception as ex:
    print('error')  """

try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('call agrega_alumno(%s,%s,%s,%s)',('xxx','222','sss', '2023-03-09 17:59:08'))

    connection.commit()    
    connection.close()
    
except Exception as ex:
    print('error') 