# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio

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
        """
        anterior
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        if (self.regla_1(socio) and self.regla_2(socio) and self.regla_3()):
            self.datos.alta(socio)
            return True
        else:
            return None

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        socio_deleted = self.buscar(id_socio)
        if socio_deleted is None:
            return False
        return self.datos.baja(id_socio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_2(socio) and (self.datos.modificacion(socio) is not None):
            return True
        return False

    def resetTabla(self):
        self.base.drop_all(self.engine)



    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        #tengo q comprobar si el buscar_dni funciona correctamente y dps si encuentra el socio_repe
        socio_repe = self.buscar_dni(socio.dni)
        if socio_repe == None:
            return True
        else:
                #levanto excepcion
            raise DniRepetido('Dni ya registrado')



    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(socio.nombre) < self.MIN_CARACTERES or len(socio.nombre)> self.MAX_CARACTERES):
            raise LongitudInvalida('ERROR. La longitud del nombre debe tener entre 3 y 15 caracteres.')
        elif (len(socio.apellido) < self.MIN_CARACTERES or len(socio.apellido)> self.MAX_CARACTERES):
            raise LongitudInvalida('ERROR. La longitud del apellido debe tener entre 3 y 15 caracteres.')
        return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.datos.todos()) > self.MAX_SOCIOS:
            #Excepción de maximo socios
            raise MaximoAlcanzado('ERROR: Se excedio la cantidad maxima de socios')
        else:
            return True

