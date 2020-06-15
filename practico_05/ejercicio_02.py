
# Implementar los metodos de la capa de datos de socios.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base,Socio
from sqlalchemy import exc

class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        if(self.session.query(Socio).filter(Socio.id == id_socio).count()>=1):
            return self.session.query(Socio).filter(Socio.id == id_socio).first()
        else:
            return None

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        if (self.session.query(Socio).filter(Socio.dni == dni_socio).count() >= 1):
            return self.session.query(Socio).filter(Socio.dni == dni_socio).first()
        else:
            return None

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        todos = self.session.query(Socio).all()
        for obj in todos:
            print(obj.id,obj.nombre, obj.apellido,obj.dni)
        return todos

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        "Socio es la tabla"
        self.session.query(Socio).delete()
        self.session.commit()
        if(self.session.query(Socio).count()==0):
            return True
        else: return False

    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        socio2 = Socio()
        socio2.dni = socio.dni
        socio2.nombre = socio.nombre
        socio2.apellido = socio.apellido
        try:
            self.session.add(socio2)
            self.session.commit()
        except exc.IntegrityError:
            self.session.rollback()
            socio2 = self.buscar_dni(socio.dni)
        return socio2

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        if(self.session.query(Socio).filter(Socio.id == id_socio).count()>=1):
            self.session.query(Socio).filter(Socio.id == id_socio).delete()
            self.session.commit()
            return True
        else:
            return False

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """

        if(self.session.query(Socio).filter(Socio.id == socio.id).count() == 1):
            socioActualizado = self.session.query(Socio).filter(Socio.id == socio.id).first()
            socioActualizado.dni = socio.dni
            socioActualizado.nombre = socio.nombre
            socioActualizado.apellido = socio.apellido
            self.session.add(socioActualizado)
            self.session.commit()
            return socio
        else:
            return False


def test():
    # alta
    socio = DatosSocio().alta(Socio(dni=38134148, nombre='Joaquin', apellido='Suarez'))
    assert socio.id > 0

    # baja
    # poner el id de socio a borrar
    assert DatosSocio().baja(socio.id) == True

    # buscar
    socio_2 = DatosSocio().alta(Socio(dni=39277486, nombre='Juan', apellido='Cruz'))
    assert DatosSocio().buscar(socio_2.id).id == socio_2.id

    # buscar dni
    socio_2 = DatosSocio().alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert DatosSocio().buscar_dni(socio_2.dni).dni == socio_2.dni

    # modificacion
    socio_3 = DatosSocio().alta(Socio(dni=11325870, nombre='Carlos', apellido='Gimenez'))
    socio_3.nombre = 'Anselmo'
    socio_3.apellido = 'Falopa'
    socio_3.dni = 13527412
    DatosSocio().modificacion(socio_3)
    socio_3_modificado = DatosSocio().buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Anselmo'
    assert socio_3_modificado.apellido == 'Falopa'
    assert socio_3_modificado.dni == 13527412

    # todos
    assert len(DatosSocio().todos()) == 3

    # borrar todos
    DatosSocio().borrar_todos()
    assert len(DatosSocio().todos()) == 0


if __name__ == '__main__':
    test()
