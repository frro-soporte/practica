from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Time, Sequence, ForeignKey, Table, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.oracle import BLOB

Base = declarative_base()

class Ciudad(Base):

    __tablename__="ciudades"
    idCiudad = Column(Integer, primary_key=True, autoincrement=True)
    pais = Column(String(100))
    provincia = Column(String(100))
    nombre = Column(String(100))
    codigoPostal = Column(Integer)


class Sacerdote(Base):
    def __init(self,dni):
        self.centrosyDisponibilidad = []
        self.dni = dni
    
    __tablename__="sacerdotes"   
    dni=Column(Integer,primary_key=True)
    apellidoNombre=Column(String(100))
    mail=Column(String(100))
    celular=Column(Integer)
    idCiudad = Column(Integer, ForeignKey('ciudades.idCiudad'))

   

class Centro(Base):
    def __init(self,dni):
        self.sacerdotesyDisponibilidad = []

    __tablename__="centros"
    idCentro = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    direccion = Column(String(100))
    sexoAtencion = Column(String(100))
    idCiudad = Column(Integer, ForeignKey('ciudades.idCiudad'))
   




class Turno(Base):
    __tablename__="turnos"
    idTurno = Column('idTurno', Integer, primary_key = True, autoincrement = True)
    dni = Column('dni', Integer)
    idCentro = Column('idCentro', Integer)
    mail =  Column('mail', String(100))
    fechayHoraTurno = Column('fechayHoraTurno', DateTime)
    descripcionSacerdote = Column('descripcionSacerdote', String(250), nullable=True)
    descricpcionPenitente = Column('descricpcionPenitente', String(250), nullable=True)

class Disponibilidad(Base):
    __tablename__ = "disponibilidades"
    idDisponibilidad = Column('idDisponibilidad', Integer, primary_key=True, autoincrement=True)
    dni = Column('dni', Integer, ForeignKey('sacerdotes.dni'))
    idCentro = Column('idCentro', Integer, ForeignKey('centros.idCentro'))
    diaAtencion = Column('diaAtencion', Integer)
    diaNombre = Column('diaNombre', String(30))
    horaInicioAtencion = Column('horaInicioAtencion', Time)
    horaFinAtencion = Column('horaFinAtencion', Time)

    sacerdote = relationship(Sacerdote)
    centro = relationship(Centro)


class Penitente(Base):
    __tablename__="penitentes"
    mail = Column(String(100), primary_key=True)
    nombreApellido = Column(String(100))
    celular = Column(String(100))
    estado = Column(Boolean) 
    sexo = Column(String(100))


#if __name__ == '__main__':