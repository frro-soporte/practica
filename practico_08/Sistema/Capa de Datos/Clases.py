from sqlalchemy import create_engine, orm
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
    def __init(self):
        self.centrosyDisponibilidad = []

    __tablename__="sacerdotes"   
    idSacerdote = Column(Integer,primary_key=True, autoincrement = True)
    apellidoNombre = Column(String(100))
    mail = Column(String(100))
    celular = Column(Integer)
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
    idSacerdote = Column('idSacerdote', Integer, ForeignKey('sacerdotes.idSacerdote'))
    idCentro = Column('idCentro', Integer, ForeignKey('centros.idCentro'))
    mail =  Column('mail', String(100))
    fechayHoraTurno = Column('fechayHoraTurno', DateTime)
    descripcionSacerdote = Column('descripcionSacerdote', String(250), nullable=True)
    descricpcionPenitente = Column('descricpcionPenitente', String(250), nullable=True)
    estado = Column('estado', String(250), nullable=True)

class Disponibilidad(Base):

    @orm.reconstructor
    def init_on_load(self):
        if (self.diaAtencion == 0):
            self.diaNombre = "Lunes"
        elif(self.diaAtencion  == 1):
            self.diaNombre = "Martes"
        elif(self.diaAtencion  == 2):
            self.diaNombre = "Miercoles"
        elif(self.diaAtencion  == 3):
            self.diaNombre = "Jueves"
        elif(self.diaAtencion  == 4):
            self.diaNombre = "Viernes"
        elif(self.diaAtencion == 5):
            self.diaNombre = "Sabado"
        elif(self.diaAtencion == 6):    
            self.diaNombre = "Domingo"
   
    __tablename__ = "disponibilidades"
    idDisponibilidad = Column('idDisponibilidad', Integer, primary_key=True, autoincrement=True)
    idSacerdote = Column('idSacerdote', Integer, ForeignKey('sacerdotes.idSacerdote'))
    idCentro = Column('idCentro', Integer, ForeignKey('centros.idCentro'))
    diaAtencion = Column('diaAtencion', Integer)
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