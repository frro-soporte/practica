# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import sqlite3
import datetime


from ejercicio_01 import borrar_tabla
from ejercicio_01 import reset_tabla
conn = sqlite3.connect('tabla.db')
cur = conn.cursor()


borrar_tabla()
def agregar_persona(nombre, nacimiento, dni, altura):
    sql = '''INSERT INTO tablaPersona (nom, nac, dni, alt) 
    VALUES (?, ?, ?, ?)
    '''
    dat = (nombre, nacimiento, dni, altura)
    cur.execute(sql, dat)
    c=cur.lastrowid
    conn.commit()
    return c


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    aa = 'SELECT * FROM tablaPersona'
    cur.execute(aa)
    x = cur.fetchall()
    print(x)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
