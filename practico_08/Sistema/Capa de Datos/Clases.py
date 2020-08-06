from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey, Table, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

SacerdoteCentro= Table('sacerdotesCentros', Base.metadata,
     Column('idSC', Integer, primary_key=True, autoincrement=True),
     Column('dni', Integer),
     Column('idCentro', Integer),
     Column('rangoAtencionSacerdote', String(100)),
     Column('rangoAtencionCentro', String(100), nullable=True),

     ForeignKeyConstraint(
        ['dni'], ['sacerdotes.dni'],
        name='fk_sacerdotesCentros_sacerdotes'
        ),
     ForeignKeyConstraint(
        ['idCentro'], ['centros.idCentro'],
        name='fk_sacerdotesCentros_centros'
        )
        
     )


class Sacerdote(Base):
    __tablename__="sacerdotes"   
    dni=Column(Integer,primary_key=True)
    nombreApellido=Column(String(100))
    mail=Column(String(100))
    celular=Column(Integer)
   
    centros = relationship("Centro", back_populates='sacerdotes', secondary=SacerdoteCentro)


class Centro(Base):
    __tablename__="centros"
    idCentro = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    direccion = Column(String(100))
    codPostal = Column(String(100))
    sexoAtencion = Column(String(100))

    sacerdotes = relationship("Sacerdote",back_populates='centros', secondary=SacerdoteCentro)



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


 

  