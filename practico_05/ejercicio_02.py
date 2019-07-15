# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base, Socio
#from ejercicio_01 import Base, Socio

class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)
        # Socio.borrar_tabla(Socio)

        # borrar_tabla(Socio)
        
    def buscar(self, id_socio):
        soc = self.session.query(Socio).filter(Socio.id == id_socio).first()
        if soc == None:
            return None
        else:
            return soc
       

    def buscar_dni(self, dni_socio):
        soc = self.session.query(Socio).filter(Socio.dni == dni_socio).first()
        if soc == None:
            return None
        else:
            return soc

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        list = []
        try:
            lista = self.session.query(Socio).all()
            for s in lista:
                list.append((s.dni,s.nombre,s.apellido))

            return list
        except:
            return list
    

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
         """
        Socio.__table__.drop()

    def alta(self, socio):
        soc = Socio()
        soc.dni = socio.dni
        soc.nombre = socio.nombre
        soc.apellido = socio.apellido
        self.session.add(soc)
        self.session.commit()
        return soc

    def baja(self, id_socio):
        soc = self.session.query(Socio).filter(Socio.id == id_socio).first()
        if soc == None:
            return False
        else:
       # session.delete(lp.id_persona)
            self.session.delete(soc)
            self.session.commit()
            return True
            return False

    def modificacion(self, socio):
        soc = self.session.query(Socio).filter(Socio.id == socio.id).first()
        if soc == None:
            return False
        else:
            soc.nombre = socio.nombre
            soc.apellido = socio.apellido
            soc.dni = socio.dni
            self.session.commit()
            return True


def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0
    # # baja
    assert datos.baja(socio.id) == True
    
    # buscar por id
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni
    # socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar_dni(socio_2.dni) == socio_2
    
    # # modificacion
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

    # # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0

if __name__ == '__main__':
    pruebas()
