from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship

Base=declarative_base()

SacerdoteCentro= Table('SacerdotesCentros', Base.metadata,
    Column('dni', Integer, ForeignKey('Sacerdotes.dni')),
    Column('idCentro', Integer, ForeignKey('Centros.idCentro')),
    Column('rangoAtencionSacerdote', String),
    Column('rangoAtencionCentro', String, nullable=True)
    )


Turno = Table('Turnos', Base.metadata,
    Column('dni', Integer, ForeignKey('Sacerdotes.dni')),
    Column('idCentro', Integer, ForeignKey('Centros.idCentro')),
    Column('mail', String, ForeignKey('Penitentes.mail')),
    Column('fechayHoraTurno', DateTime),
    Column('descripcionSacerdote', String, nullable=True),
    Column('descricpcionPenitente', String, nullable=True)
    )

class Sacerdote(Base):
    __tablename__="Sacerdotes"   
    dni=Column(Integer,primary_key=True)
    nombreApellido=Column(String)
    mail=Column(String)
    celular=Column(Integer)
   
    centrosR = relationship("Centro", back_populates='Centros', secondary=SacerdoteCentro)
    turnosR = relationship("Turnos", back_populates='Turnos', secondary=Turno)

class Centro(Base):
    __tablename__="Centros"
    idCentro = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    direccion = Column(String)
    codPostal = Column(String)
    sexoAtencion = Column(String)

    sacerdotesR = relationship("Sacerdotes",back_populates='Sacerdotes', secondary=SacerdoteCentro)
    turnosR = relationship("Turnos", back_populates='Turnos', secondary=Turno)

class Penitente(Base):
    __tablename__="Penitentes"
    mail = Column(String, primary_key=True)
    nombreApellido = Column(String)
    celular = Column(String)
    estado = Column(String)
    sexo = Column(String)

    turnosR = relationship("Turnos", back_populates='Turnos', secondary=Turno)


    