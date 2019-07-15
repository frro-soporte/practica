# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime

class DniRepetido(Exception):
    pass
class LongitudInvalida(Exception):
    pass

class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        Base = declarative_base()
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)
        self.datos = DatosSocio()

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
        list = []
        try:
            lista = self.session.query(Socio).all()
            for s in lista:
                list.append((s.dni,s.nombre,s.apellido))
            return list
        except:
            return list
    

    
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


    def regla_1(self, socio):
        try:
            socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
            return False
        except Exception as e:
            raise DniRepetido('Dni Repetido')
            return True

    def regla_2(self, socio):
        
        try:
            assert len(socio.nombre) < self.MAX_CARACTERES and len(socio.nombre) > self.MIN_CARACTERES
            assert len(socio.apellido) < self.MAX_CARACTERES and len(socio.apellido) > self.MIN_CARACTERES
            return True
        except Exception as e:
            raise LongitudInvalida('Longitud invalida')
            return False


    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        self.MAX_SOCIOS

        return False
