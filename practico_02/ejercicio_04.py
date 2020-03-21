# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).
from practico_02.ejercicio_03 import Persona
from datetime import datetime


class Estudiante(Persona):

    def __init__(self, nombre: str, edad: int, sexo: str, peso: float, altura: float,
                 carrera: str, anio: str, cantidad_materias: int, cantidad_aprobadas: int):
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

        Persona.__init__(self, nombre, edad, sexo, peso, altura)

    def avance(self):
        avance = self.cantidad_aprobadas / self.cantidad_materias
        porcentaje = avance * 100
        return round(porcentaje, 2)

    # implementar usando modulo datetime
    def edad_ingreso(self):
        anio_ingreso = datetime.strptime(self.anio, "%Y").year
        anio__actual = datetime.utcnow().year
        anios_cursados = anio__actual - anio_ingreso

        return self.edad - anios_cursados


assert Estudiante("pedro", 24, "H", 98, 18, "Sistemas", "2018", 18, 6).edad_ingreso() == 22
