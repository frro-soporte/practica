# Implementar los metodos de la capa de negocio de socios.

from ejercicio_01 import Socio
from ejercicio_02 import DatosSocio
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class DniRepetido(Exception):
    # print("".format(Exception +"  - El DNI ya se encuentra ingresado para otro socio, verifique."))
    pass


class LongitudInvalida(Exception):
    # print("".format(Exception +"  - El nombre y/o el apellido del socio tienen una longitud inválida, la misma debe estar comprendida entre" +  MIN_CARACTERES + " y " + MAX_CARACTERES))
    pass


class MaximoAlcanzado(Exception):
    # print("".format(Exception +"  - Se ha alcanzado el máximo de socios que pueden darse de alta."))
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
        if not self.regla_1(socio):
            return False
        if not self.regla_2(socio):
            return False
        if not self.regla_3():
            return False

        try:
            self.datos.alta(socio)
        except:
            print("Error inesperado " + e)

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
        if datos.baja(id_socio):
            return True
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return False

    def modificacion(self, socio):
        try:
            if regla_2(socio):
                if datos.modificacion(socio):
                    return True
            else:
                raise LongitudInvalida
        except:
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
        if socio is not None:
            raise DniRepetido
            return False
        else:
            return True
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """

    def regla_2(self, socio):
        nombre = socio.nombre
        # try:
        if len(socio.nombre) <= self.MIN_CARACTERES or len(socio.nombre) >= self.MAX_CARACTERES:
            raise LongitudInvalida
        if len(socio.apellido) <= self.MIN_CARACTERES or len(socio.apellido) >= self.MAX_CARACTERES:
            raise LongitudInvalida

        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        return True

    def regla_3(self):
        socios = self.datos.todos()
        if len(socios) > self.MAX_SOCIOS:
            raise MaximoAlcanzado
            return False
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        return True
