# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime

from ejercicio_01 import Persona, session, crear_tabla, borrar_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    per = Persona()
    per.nombre = nombre
    per.fechaNacimiento = nacimiento
    per.dni = dni
    per.altura = altura
    session.add(per)
    session.commit()
    #p = session.query(Persona).all()
    #print("Lista de Personas: ")
    #for p in lp:
    #    print("Persona ",p.id,p.nombre,p.fechaNacimiento,p.dni,p.altura)
    return per.id


#@reset_tabla
def pruebas():
    crear_tabla()
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.date(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan
    borrar_tabla()

if __name__ == '__main__':
    pruebas()
