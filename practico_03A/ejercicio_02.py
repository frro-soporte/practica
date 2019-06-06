# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.


from ejercicio_01 import reset_tabla, Persona, borrar_tabla
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Date, Integer, ForeignKey, String, Table
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///tabla.db', echo=True)
Base = declarative_base()

#borrar_tabla()
def agregar_persona(nombre, nacimiento, dni, altura, session):
    per = Persona(nombre,nacimiento,dni,altura)
    session.add(per)
    session.commit()
    session.refresh(per)
    id=per.idPer
    return id

@reset_tabla
def pruebas(session):
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180,session)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195,session)
    print(id_juan, id_marcela)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()

