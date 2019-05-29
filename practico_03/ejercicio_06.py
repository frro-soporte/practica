# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from ejercicio_01 import borrar_tabla, crear_tabla, Base, Persona, engine
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class PersonaPeso(Base):
    __tablename__ = 'PersonaPeso'
    id = Column(Integer,primary_key=True)
    idPer = Column(Integer,ForeignKey('Persona.id'))
    fecha = Column(Date,nullable=False)
    peso = Column(Integer,nullable=False)
    perPeso = relationship(Persona)

def crear_tabla_peso():
    Base.metadata.create_all(engine)


def borrar_tabla_peso():
    PersonaPeso.__table__.drop(engine)


crear_tabla()
crear_tabla_peso()
borrar_tabla_peso()
borrar_tabla()

