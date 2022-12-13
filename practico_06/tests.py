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
        #valida regla
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(socio))
        #repite dni
        self.ns.alta(socio)
        error = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, error)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(correcto))

        # nombre menor a 3 caracteres
        error = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, error)

    def test_regla_2_nombre_mayor_15(self):
         # valida regla
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(correcto))

        # nombremayor a 15 caracteres
        error = Socio(dni=12345678, nombre='Juaaaaaaaaaaaaaaaaaaaaaaaaaan', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, error)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(correcto))

        # apellido menor a 3 caracteres
        error = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, error)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(correcto))

        # apellido mayor a 15 caracteres
        error = Socio(dni=12345678, nombre='Juan', apellido='Peeeeeeeeeeeeeeeeeeeeeeeeeeeerez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, error)


    def test_regla_3(self):
        # valida regla
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(correcto)
        self.assertTrue(self.ns.regla_3())

        #mas de 200 socios
        a=12345679
        for y in range(0, 200):
            error = Socio(dni=a,nombre='Juan', apellido='Perez')
            self.ns.alta(error)
            a=a+1
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)

    def test_baja(self):
        # valida baja
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(correcto)
        self.assertTrue(self.ns.baja(correcto.id))

        #borra socio no cargado
        error = Socio(dni =12345678, nombre='Juan', apellido='Perez')
        self.assertFalse(self.ns.baja(error.id))

    def test_buscar(self):
        # valida buscar
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(correcto)
        self.assertTrue(self.ns.buscar(correcto.id))

        #busca socio no cargado
        error = Socio(dni = 444444444, nombre='Juan', apellido='Perez')
        self.assertFalse(self.ns.buscar(error.id))

    def test_buscar_dni(self):
        # valida busqueda por dni
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(correcto)
        self.assertTrue(self.ns.buscar_dni(correcto.dni))

        # busca por dni un socio que no se ha cargado
        error = Socio(dni = 41028971, nombre='Bruno', apellido='Caracini')
        self.assertFalse(self.ns.buscar_dni(error.dni))


    def test_todos(self):
        # valida devolucion de un arreglo de socios no vacio
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(correcto)
        assert self.ns.todos() != None


    def test_modificacion(self):
        # valida modificacion
        correcto = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(correcto)
        modi = Socio(dni=12345679, nombre='Juan Andres', apellido='Perez')
        #self.assertTrue(self.ns.modificacion(modi))

        # modifica socio que no existe
        error = Socio(dni = 44444444, nombre='Juan', apellido='Perez')
        self.assertFalse(self.ns.modificacion(error))

