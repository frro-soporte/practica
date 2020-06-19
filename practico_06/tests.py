# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        #Regla 1: no puede haber dos socios con el mismo DNI
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        #DNI repetido
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)

        #DNI no repetido
        valido = Socio(dni=20402685, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))

    def test_regla_2_nombre_menor_3(self):
        # Regla 2: nombre mayor a 3 caracteres
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        #Regla 2: nombre menor a 15 caracteres
        valido = Socio(dni=36370135, nombre='Ana', apellido='Domingo')
        self.assertTrue(self.ns.regla_2(valido))

        #Nombre mayor a 15 caracteres
        invalido = Socio(dni=36370135, nombre='HolaMeLlamoAnaClara', apellido='Domingo')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        #Regla 2: apellido mayor a 3 caracteres
        valido = Socio(dni=36370135, nombre='Ana', apellido='Domingo')
        self.assertTrue(self.ns.regla_2(valido))

        #Apellido menor a 3 caracteres
        invalido = Socio(dni=36370135, nombre='Ana', apellido='Ba')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
         #Regla 2: apellido menor a 15 caracteres
        valido = Socio(dni=23111111, nombre='Luciano', apellido='Gorza')
        self.assertTrue(self.ns.regla_2(valido))

        #Apellido mayor a 15 caracteres
        invalido = Socio(dni=231111111, nombre='Luciano', apellido='Este Es Un Apellido Muy Largo')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        #Regla  3: no puede excederse la cantidad máxima de socios
        socio = Socio(dni=36370135, name='Ana', apellido='Domingo')
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3, socio)

    def test_baja(self):
        # pre-condiciones: tener un socio cargado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # ejecuto la lógica
        resultado = self.ns.baja(1)

        # post-condiciones: el socio fue dado de baja en la base de datos
        self.assertTrue(resultado)
        self.assertEqual(len(self.ns.todos()), 0)

    def test_buscar(self):
        # pre-condiciones: tener un socio cargado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # ejecuto la lógica
        resultado = self.ns.buscar(1)

        # post-condiciones: se encontró al socio cuyo id se ingresó
        self.assertEqual(socio.dni, resultado.dni)

    def test_buscar_dni(self):
        # pre-condiciones: tener un socio cargado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # ejecuto la lógica
        resultado = self.ns.buscar_dni(12345678)

        # post-condiciones: se encontró al socio cuyo dni se ingresó
        self.assertEqual(socio.dni, resultado.dni)

    def test_todos(self):
        # pre-condiciones: tener al menos un socio cargado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # ejecuto la lógica
        resultado = self.ns.todos()

        # post-condiciones: devuelve la cantidad de socios ingresados
        self.assertEqual(len(resultado), 1)

    def test_modificacion(self):
        # pre-condiciones: tener un socio cargado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        socio_modificado = self.ns.datos.buscar_dni(12345678)
        socio_modificado.nombre = 'José'

        # ejecuto la lógica
        resultado = self.ns.modificacion(socio_modificado)

        self.assertTrue(resultado)

unittest.main()