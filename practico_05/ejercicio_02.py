# Implementar los metodos de la capa de datos de socios.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, id_socio):
        try:
            socio = self.session.query(Socio).get(id_socio)
            return socio
        except:
            return None

    def buscar_dni(self, dni_socio):
        try:
            socio = self.session.query(Socio).filter(Socio.dni==dni_socio).first()
            return socio
        except:
            return None

    def todos(self):
        socios = self.session.query(Socio).all()
        return socios

    def borrar_todos(self):
        try:
            self.session.query(Socio).delete()
            return True
        except:
            return False

    def alta(self, socio):
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio):
        socio = self.buscar(id_socio)
        self.session.delete(socio)
        return True

    def modificacion(self, socio):
        socio_modificado = self.buscar(socio.id_socio)
        socio_modificado.dni = socio.dni
        socio_modificado.nombre = socio.nombre
        socio_modificado.apellido = socio.apellido
        self.session.commit()
        return socio_modificado

def pruebas():

    # alta
    datos = DatosSocio()
    datos.borrar_todos()

    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id_socio > 0

    # baja
    assert datos.baja(socio.id_socio) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id_socio) == socio_2

    # buscar dni
    # socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar_dni(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id_socio)
    assert socio_3_modificado.id_socio == socio_3.id_socio
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0

if __name__ == '__main__':
    pruebas()
