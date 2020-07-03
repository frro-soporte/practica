from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base=declarative_base()

class Sacerdote(Base):
    __tablename__="Sacerdotes"   
    dni=Column(Integer,primary_key=True)
    nombreApellido=Column(String)
    mail=Column(String)
    celular=Column(Integer)
   
    centros=relationship("Centro",back_populates='centros')

class Centro(Base):
    __tablename__="Centros"
    idCentro = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    direccion = Column(String)
    codPostal = Column(String)
    sexoAtencion = Column(String)

    sacerdotes=relationship("Sacerdotes",back_populates='Sacerdotes')

class Penitente(Base):
    __tablename__="Penitentes"
    mail = Column(String, primary_key=True)
    nombreApellido = Column(String)
    celular = Column(String)
    estado = Column(String)
    sexo = Column(String)

