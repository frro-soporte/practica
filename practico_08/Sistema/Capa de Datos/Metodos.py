from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Clases import Base, Sacerdote, Penitente, Centro

class Datos():
    def __init__(self):
        engine = create_engine('sqlite:///turnosConfesiones.db')
        Base.metadata.drop_all(engine) #Elimina todo lo que pueda tener el motor
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine) #crea todas las tablas que todavia no existen
        

class DatosPenitentes(Datos):
    pass

class DatosSacerdotes(Datos):
    pass
class DatosCursos(Datos):
    pass

if __name__ == '__main__':
    datos = Datos()
  