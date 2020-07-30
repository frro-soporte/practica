from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey, Table, Boolean
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

SacerdoteCentro= Table('SacerdotesCentros', Base.metadata,
     Column('dni', Integer, ForeignKey('Sacerdotes.dni')),
     Column('idCentro', Integer, ForeignKey('Centros.idCentro')),
     Column('rangoAtencionSacerdote', String(100)),
     Column('rangoAtencionCentro', String(100), nullable=True)
     )


class Sacerdote(Base):
    __tablename__="Sacerdotes"   
    dni=Column(Integer,primary_key=True)
    nombreApellido=Column(String(100))
    mail=Column(String(100))
    celular=Column(Integer)
   
    centros = relationship("Centro", back_populates='sacerdotes', secondary=SacerdoteCentro)
    turnos = relationship("Turnos")
    

class Centro(Base):
    __tablename__="Centros"
    idCentro = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    direccion = Column(String(100))
    codPostal = Column(String(100))
    sexoAtencion = Column(String(100))

    sacerdotes = relationship("Sacerdotes",back_populates='centros', secondary=SacerdoteCentro)
    turnos = relationship("Turnos")


class Turno(Base):
    __tablename__="Turnos"
    dni = Column('dni', Integer, ForeignKey('Sacerdotes.dni'), primary_key=True)
    idCentro = Column('idCentro', Integer, ForeignKey('Centros.idCentro'), primary_key=True)
    mail =  Column('mail', String(100), ForeignKey('Penitentes.mail'), primary_key=True)
    fechayHoraTurno = Column('fechayHoraTurno', DateTime)
    descripcionSacerdote = Column('descripcionSacerdote', String(250), nullable=True)
    descricpcionPenitente = Column('descricpcionPenitente', String(250), nullable=True)  


class Penitente(Base):
    __tablename__="Penitentes"
    mail = Column(String(100), primary_key=True)
    nombreApellido = Column(String(100))
    celular = Column(String(100))
    estado = Column(Boolean) 
    sexo = Column(String(100))

    turnos = relationship("Turnos")

class Turno(Base):
    __tablename__="Turnos"
    dni = Column('dni', Integer, ForeignKey('Sacerdotes.dni'), primary_key=True)
    idCentro = Column('idCentro', Integer, ForeignKey('Centros.idCentro'), primary_key=True)
    mail =  Column('mail', String, ForeignKey('Penitentes.mail'), primary_key=True)
    fechayHoraTurno = Column('fechayHoraTurno', DateTime)
    descripcionSacerdote = Column('descripcionSacerdote', String, nullable=True)
    descricpcionPenitente = Column('descricpcionPenitente', String, nullable=True) 

  