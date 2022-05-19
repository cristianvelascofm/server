from django.db import connection
from bd import get_connection

import json

def get_user():
    connection = get_connection()
    user = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT usrCedula,usrPrimerNombre,usrSegundoNombre,usrPrimerApellido,usrSegundoApellido,usrClave,usrEmail,usrNitEmpresa,usrRol,usrEstado FROM usuario")
        user = cursor.fetchall()
        ans = json.dumps(user)
    print('AA: ',ans)
    connection.close()
    return ans


def add_user(cedula,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,clave,email,nit_empresa,rol,estado):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO usuario(usrCedula,usrPrimerNombre,usrSegundoNombre,usrPrimerApellido,usrSegundoApellido,usrClave,usrEmail,usrNitEmpresa,usrRol,usrEstado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(cedula,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,clave,email,nit_empresa,rol,estado))
    connection.commit()
    connection.close()