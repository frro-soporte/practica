# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

#from practico_03.ejercicio_02 import agregar_persona
#from practico_03.ejercicio_06 import reset_tabla
from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_04 import buscar_persona
import sqlite3

def agregar_peso(id_persona, fecha, peso):
    db = sqlite3.connect('persona_db.sqlite')
    cursor = db.cursor()
    persona = buscar_persona(id_persona)
    
    if persona == False:
        return False
    else:
        cSQL = 'SELECT * FROM persona_peso WHERE id_persona = ? and fecha_pesaje > ?'
        cursor.execute(cSQL, (id_persona, fecha,))
        pesaje_anterior = cursor.fetchone()
       
        if pesaje_anterior == None:
        #cursor = db.cursor()
            cSQL = 'INSERT INTO persona_peso (id_persona, fecha_pesaje, peso)' \
               'VALUES (?,?,?)'
            tdatos = (id_persona, fecha, peso)
            cursor.execute(cSQL, tdatos)
            id = cursor.lastrowid
            
            db.commit()
            return id
        else:
            return False



@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    #assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False
    assert agregar_peso(id_juan, '2018-05-16 00:00:00', 80) == False
    

if __name__ == '__main__':
    pruebas()
