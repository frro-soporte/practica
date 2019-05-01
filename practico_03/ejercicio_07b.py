# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_01 import conexion
from practico_03.ejercicio_04 import buscar_persona

def agregar_peso(id_persona, fecha, peso):
    print(validate_date(id_persona, fecha))

    print("Persona que busqué",buscar_persona(id_persona))

    if (validate_date(id_persona, fecha) and buscar_persona(id_persona)):
        con = conexion()
        c = con.cursor()
        query = "INSERT INTO PersonaPeso(idPersona, fecha, peso) VALUES (?,?,?)"
        c.execute(query, ((id_persona, datetime.datetime.strftime(fecha, "%Y-%m-%d"), peso)))
        c.close()
        con.commit()
        con.close()
        return c.lastrowid
    else:
        return False

    pass

def validate_date (id_persona, fecha):
    con = conexion()
    c = con.cursor()
    query = "Select * from PersonaPeso where idPersona = ?"
    res = c.execute(query, (id_persona,))

    data = c.fetchone()
    print(data)
    fecha = datetime.datetime.strftime(fecha, "%Y-%m-%d")
    if (data[1] >= fecha):
        return False
    else:
        return True

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()