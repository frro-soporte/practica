from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Time, Sequence, ForeignKey, Table, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.oracle import BLOB

Base = declarative_base()

class Disponibilidad(Base):
    __tablename__ = "disponibilidades"
    idSC = Column('idSC', Integer, primary_key=True, autoincrement=True)
    dni = Column('dni', Integer)
    idCentro = Column('idCentro', Integer)
    diaAtencion = Column('diaAtencion', Integer)
    horaInicioAtencion = Column('horaInicioAtencion', Time)
    horaFinAtencion = Column('horaFinAtencion', Time)


    ForeignKeyConstraint(
        ['dni'], ['sacerdotes.dni'],
        name='fk_disponibilidades_sacerdotes'
        ),
    ForeignKeyConstraint(
        ['idCentro'], ['centros.idCentro'],
        name='fk_diponibilidades_centros'
        )

class Ciudad(Base):
    __tablename__="ciudades"
    idCiudad = Column(Integer, primary_key=True, autoincrement=True)
    pais = Column(String(100))
    provincia = Column(String(100))
    nombre = Column(String(100))
    codigoPostal = Column(Integer)

class Sacerdote(Base):
    __tablename__="sacerdotes"   
    dni=Column(Integer,primary_key=True)
    nombreApellido=Column(String(100))
    mail=Column(String(100))
    celular=Column(Integer)
    imagen = Column(BLOB)
    idCiudad = Column(Integer)
   
    centros = relationship("Centro", back_populates='sacerdotes', secondary=Disponibilidad)

    ForeignKeyConstraint(
    ['idCiudad'], ['ciudades.idCiudad'],
    name='fk_sacerdotes_ciudades'
    )


class Centro(Base):
    __tablename__="centros"
    idCentro = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    direccion = Column(String(100))
    codPostal = Column(String(100))
    sexoAtencion = Column(String(100))
    imagen = Column(BLOB)
    idCiudad = Column(Integer)

    sacerdotes = relationship("Sacerdote",back_populates='centros', secondary=Disponibilidad)
   
    ForeignKeyConstraint(
    ['idCiudad'], ['ciudades.idCiudad'],
    name='fk_centros_ciudades'
    )



class Turno(Base):
    __tablename__="turnos"
    idTurno = Column('idTurno', Integer, primary_key = True, autoincrement = True)
    dni = Column('dni', Integer)
    idCentro = Column('idCentro', Integer)
    mail =  Column('mail', String(100))
    fechayHoraTurno = Column('fechayHoraTurno', DateTime)
    descripcionSacerdote = Column('descripcionSacerdote', String(250), nullable=True)
    descricpcionPenitente = Column('descricpcionPenitente', String(250), nullable=True)
    
    ForeignKeyConstraint(
    ['dni'], ['sacerdotes.dni'],
    name='fk_turnos_sacerdotes'
    ),
    ForeignKeyConstraint(
    ['idCentro'], ['centros.idCentro'],
    name='fk_turnos_centros'
    ),
    ForeignKeyConstraint(
    ['mail'], ['penitentes.mail'],
    name='fk_turnos_penitentes'
    )  




class Penitente(Base):
    __tablename__="penitentes"
    mail = Column(String(100), primary_key=True)
    nombreApellido = Column(String(100))
    celular = Column(String(100))
    estado = Column(Boolean) 
    sexo = Column(String(100))


 

  