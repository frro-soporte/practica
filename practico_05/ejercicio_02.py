# Implementar los metodos de la capa de datos de socios.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        self.base = Base.metadata
        self.engine = engine

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.session.query(Socio).get(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.session.query(Socio).filter(Socio.dni == dni_socio).one_or_none()

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        socios_searched = self.session.query(Socio).all()
        list_socios = []
        for s in socios_searched:
            list_socios.append(s)
        return list_socios

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            self.session.query(Socio).delete()
            self.session.commit()
        except:
            return False
        finally:
            return True

    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.add(socio)
        self.session.commit()
        return self.buscar_dni(socio.dni)

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            socio_deleted = self.session.query(Socio).get(id_socio)
            self.session.delete(socio_deleted)
            self.session.commit()
        except:
            return False
        finally:
            return True

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        a_user = self.session.query(Socio).filter(Socio.id == socio.id).one_or_none()
        if a_user is None:
            return None
        a_user.dni = socio.dni
        a_user.nombre = socio.nombre
        a_user.apellido = socio.apellido
        self.session.commit()
        return self.session.query(Socio).get(socio.id)

    def resetTabla(self):
        self.base.drop_all(self.engine)



def pruebas():
    try:
        # alta
        datos = DatosSocio()
        socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        assert socio.id > 0
        print("Paso test 1")

        # baja
        assert datos.baja(socio.id) is True
        print("Paso test 2")

        # buscar
        socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
        assert datos.buscar(socio_2.id) == socio_2
        print("Paso test 3")

        # buscar dni
        assert datos.buscar_dni(socio_2.dni) == socio_2
        print("Paso test 4")

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
        print("Paso test 5")

        # todos
        assert len(datos.todos()) == 2
        print("Paso test 6")

        # borrar todos
        datos.borrar_todos()
        assert len(datos.todos()) == 0
        print("Paso test 7")

    finally:
        datos.resetTabla()




if __name__ == '__main__':
    pruebas()

