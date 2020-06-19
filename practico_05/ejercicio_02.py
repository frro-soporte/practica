# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)

    def buscar(self, id_socio):
        soc = self.session.query(Socio).filter(Socio.id == id_socio).first()
        return soc
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """

    def buscar_dni(self, dni_socio):
        soc = self.session.query(Socio).filter(Socio.dni == dni_socio).first()
        return soc

        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """

    def todos(self):
        soc = self.session.query(Socio).all()
        return soc
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """


    def borrar_todos(self):
        try:
            a = True
            c = self.session.query(Socio).all()
            for i in c:
                self.session.delete(i)
            self.session.commit()
        except:
            a = False
        return a
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """


    def alta(self, socio):
        self.session.add(socio)
        self.session.commit()
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        return socio

    def baja(self, id_socio):
        try:
            a = True
            s = self.session.query(Socio).filter(Socio.id == id_socio).first()
            self.session.delete(s)
            self.session.commit
        except:
            a = False
        return a
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """

    def modificacion(self, socio):
        a = self.session.query(Socio).filter(Socio.id == socio.id).first()
        a.dni = socio.dni
        a.nombre = socio.nombre
        a.apellido = socio.apellido
        self.session.commit
        a = self.session.query(Socio).filter(Socio.id == socio.id).first()
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        return a


def pruebas():
    # alta
    datos = DatosSocio()

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0
    assert datos.borrar_todos() == True

    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0

    # baja
    assert datos.baja(socio.id) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni
    # socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar_dni(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
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
