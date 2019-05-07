# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  # Metadatos


class DbManager(object):
    engine = create_engine('sqlite:///personadb_alquemy.db', echo=True)

    def creardb(self):
        Base.metadata.create_all(self.engine)

    def guardar(self, objeto):
        session = self.get_session()
        session.add(objeto)
        session.commit()

    def getall(self, objeto):
        session = self.get_session()
        result = session.query(objeto).all()
        return result

    def getall_id(self, objeto):
        session = self.get_session()
        result = session.query(objeto).all()
        ids = []
        for item in result:
            ids.append(item.id)
        return ids

    def delete_notin(self, objeto, ids):
        session = self.get_session()
        result = session.query(objeto).filter(objeto.id.notin_(ids)).delete()
        session.commit()

    def get_session(self):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        return session

    def existe(self, objeto, id):
        session = self.get_session()
        registros = session.query(objeto).filter(objeto.id == id).count()
        return registros

class Persona(Base):
 __tablename__ = 'persona' # ----nombre de la tabla
 # Definimos las columnas de la tabla Persona
 id_persona = Column(Integer, primary_key=True)
 nombre = Column(String(30), nullable=False)
 fecha_nac = Column(DateTime, nullable=False)
 dni = Column(Integer, nullable=False)
 altura = Column(Integer, nullable=False)

def crear_tabla(engine):

 Base.metadata.create_all(engine)

def borrar_tabla(Persona):
 # Crea todas las tablas definidas en los metadatos
 Persona.__table__.drop()




def reset_tabla(func):
    def func_wrapper():
        engine = create_engine('sqlite:///personadb_alquemy.db', echo=True)
        Base.metadata.bind = engine
        # ---- creamos una sesión para admin datos
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()
        crear_tabla(engine)

        #Corre la funcion con la tabla que creamos
        func(session)
        #Luego de finalizar la funcion elimina la tabla
        borrar_tabla(Persona)
    return func_wrapper


