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
        # valido que socio este registrado
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))

        self.ns.alta(valido)

        incorrecto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, incorrecto)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombremayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Peeeeeerrrrrreeeeeezzzzzzzzzzz')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.regla_3())

        # Se añaden mas de 200 socios
        dni = 12345678
        for y in range(0, 200):
            dni += 1
            invalido = Socio(dni=dni, nombre='Juan', apellido='Perez')
            self.ns.alta(invalido)
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)

    def test_baja(self):
        # valida baja
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.baja(valido.id))

        # borra un socio que no se ha cargado
        invalido = Socio(dni=87654321, nombre='Juan', apellido='Perez')
        self.assertFalse(self.ns.baja(invalido.id))

    def test_buscar(self):
        # valida busqueda
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.buscar(valido.id))

        # Se busca un socio que no se ha cargado
        invalido = Socio(dni=87654321, nombre='Giovanni', apellido='Martin')
        self.assertFalse(self.ns.buscar(invalido.id))

    def test_buscar_dni(self):
        # valida busqueda por dni
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.buscar_dni(valido.dni))

        # Se busca por dni un socio que no se ha cargado
        invalido = Socio(dni=87654321, nombre='Giovanni', apellido='Martin')
        self.assertFalse(self.ns.buscar_dni(invalido.dni))

    def test_todos(self):
        # valida devoucion de un arreglo de socios no vacio, cargando uno para asegurar la no nulidad de socios
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        assert self.ns.todos() is not None

    def test_modificacion(self):
        # valida modificacion de socio existente
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        valido.dni = 12345679
        valido.nombre = 'Juan'
        valido.apellido = 'Perez'
        self.assertTrue(self.ns.modificacion(valido))

        # Se modifica socio inexistente
        invalido = Socio(dni=17654321, nombre='Giovani', apellido='Martin')
        self.assertFalse(self.ns.modificacion(invalido))
