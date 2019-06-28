# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'

    # id = Column(...)
    # dni = Column(...)
    # nombre = Column(...)
    # apellido = Column(...)
