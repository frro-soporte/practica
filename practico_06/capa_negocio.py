# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


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
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        socio = self.datos.buscar(id_socio)
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return socio

    def buscar_dni(self, dni_socio):
        socio = self.datos.buscar_dni(dni_socio)
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return socio

    def todos(self):
        socios_lista = self.datos.todos()
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return socios_lista

    def alta(self, socio):
        try: 
            self.regla_1(socio)
            self.regla_2(socio)
            self.regla_3()
        except Exception as err:
            print('Hubo un error: ', err.args)
            return False

        try:
            self.datos.alta(socio)
        except Exception as err:
            print("Error: ", err)
            return False

        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        return True

    def baja(self, id_socio):
        return self.datos.baja(id_socio)
    """
    Borra el socio especificado por el id.
    Devuelve True si el borrado fue exitoso.
    :rtype: bool
    """

    def modificacion(self, socio):
        try:
            if self.regla_2(socio):
                if self.datos.modificacion(socio):
                    return True
                else:
                    return False
        except Exception as err:
            print('Error: ', err.args)
        return False

    """
    Modifica un socio.
    Se debe validar la regla 2 primero.
    Si no valida, levantar la excepcion correspondiente.
    Devuelve True si la modificacion fue exitosa.
    :type socio: Socio
    :rtype: bool
    """

    def regla_1(self, socio):
        dni = socio.dni
        socio = self.datos.buscar_dni(dni)
        if socio is None:
            return True
        else:
            raise DniRepetido('El DNI ingresado ya se encuentra registrado para otro socio, verifique.')
        return False
    """
    Validar que el DNI del socio es unico (que ya no este usado).
    :type socio: Socio
    :raise: DniRepetido
    :return: bool
    """

    def regla_2(self, socio):
        if len(socio.nombre) > self.MIN_CARACTERES and len(socio.nombre) < self.MAX_CARACTERES and len(socio.apellido) > self.MIN_CARACTERES and len(socio.apellido) < self.MAX_CARACTERES:
            return True
        else:
            raise LongitudInvalida('El nombre o el apellido ingresados no cumplen con la regla de ' + self.MIN_CARACTERES + ' mínimos y ' + self.MAX_CARACTERES + ' máximos.' )
        return False
    """
    Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
    :type socio: Socio
    :raise: LongitudInvalida
    :return: bool
    """

    def regla_3(self):
        socios = self.datos.todos()
        if len(socios) < self.MAX_SOCIOS:
            return True
        else:
            raise MaximoAlcanzado('Se ha alcanzado el máximo de socios permitidos.')
        return False
    """
    Validar que no se esta excediendo la cantidad maxima de socios.
    :raise: MaximoAlcanzado
    :return: bool
    """