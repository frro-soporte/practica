# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db', echo=True)
        Base.metadata.drop_all(engine)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, id_socio):
        try:
            return self.session.query(Socio).filter_by(id_socio=id_socio).first()
        except:
            return None

    def buscar_dni(self, dni_socio):
        try:
            return self.session.query(Socio).filter_by(dni=dni_socio).first()
        except:
            return None

    def todos(self):
        try:
            return self.session.query(Socio).all()
        except:
            return None

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
        if socio is None:
            return False
        else:
            try:
                self.session.delete(socio)
                self.session.commit()
                return True
            except:
                return False

    def modificacion(self, socio):
        socio_busqueda = self.buscar(socio.id_socio)
        socio_busqueda.dni = socio.dni
        socio_busqueda.nombre = socio.nombre
        socio_busqueda.apellido = socio.apellido
        self.session.commit()
        return socio_busqueda


def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id_socio > 0

    # baja
    assert datos.baja(socio.id_socio) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id_socio) == socio_2

    # buscar dni
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