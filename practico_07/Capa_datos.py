# Implementar los metodos de la capa de datos de socios.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tkinter import messagebox
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String, UniqueConstraint,MetaData
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Socio(Base):
    __tablename__ = 'socios'

    id = Column(Integer,primary_key=True,unique=True)
    dni = Column(Integer,unique=True)
    nombre = Column(String(250))
    apellido = Column(String(250))


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
        socio = self.session.query(Socio).filter(Socio.id == id_socio).first()
        if socio is None:
            return None
        else:
            return socio

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio = self.session.query(Socio).filter(Socio.dni == dni_socio).first()
        if socio is None:
            return None
        else:
            return socio
        

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        socios = self.session.query(Socio).all()
        if len(socios) == 0:
            return socios
        else:
            lista = []
            for s in socios:
                lista.append((s.id, s.dni,s.nombre,s.apellido))
            return lista
        


    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        soc = Socio()
        soc.dni = socio.dni
        soc.nombre = socio.nombre
        soc.apellido = socio.apellido
        self.session.add(soc)
        self.session.commit()
        return soc

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        socio = self.session.query(Socio).filter(Socio.id == id_socio).first()
        if socio is None:
            return False
        else:
            self.session.delete(socio)
            self.session.commit()
            nom = socio.nombre
            ap = socio.apellido
            messagebox.showinfo('Borrado Exitoso', 'Socio borrado con exito.')
            return True

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        old_socio = self.session.query(Socio).filter(Socio.id == socio.id).first()
        if old_socio is None:
            return False
        else:
            old_socio.nombre = socio.nombre
            old_socio.apellido = socio.apellido
            old_socio.dni = socio.dni
            self.session.commit()
            return old_socio






'''
def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0
    
    # baja
    assert datos.baja(socio.id) == True
    
    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2
    
    # buscar dni
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
'''