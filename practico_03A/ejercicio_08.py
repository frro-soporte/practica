# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Practica01Alchemy import Persona
from Practica06Alchemy import PersonaPeso
from Practica03Alchemy import agregar_persona
from Practica07Alchemy import buscar_persona
from Practica07Alchemy import agregar_peso
from Practica06Alchemy import reset_tabla
import datetime

Base = declarative_base()
engine = create_engine('mysql://root:852456ale@localhost:3306/python')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()



def listar_pesos(id_persona):
    x=buscar_persona(id_persona)
    if(x!=False):
        pesos=session.query(PersonaPeso).filter(PersonaPeso.IdPersona == id_persona).all()
        listapesos=[]
        for p in pesos:
             listapesos.append((p.Fecha,p.Peso))
        print(listapesos)
        return  listapesos
    else:
        return False




def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
