# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime, sqlite3

db = sqlite3.connect('../db/tp_03.s3db')

def buscar_persona(id_persona):
    cursor = db.cursor()
    cursor.execute('''select * from personas where idPersona=?''', (id_persona,))
    returnObject = cursor.fetchone()
    if not returnObject:
        return False
    else:
        return returnObject

assert buscar_persona(5) == False
assert buscar_persona(1) == (1, 'Ana Domingo', '1991-07-23', 36370135, 175)