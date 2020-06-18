# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).
from datetime import datetime
from practico_02.ejercicio_03 import Persona

#La funcion main esta comentada para que no interfiera en las herencias
class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        print("Promedio de la Materia Aprobada: ", round(self.cantidad_aprobadas * 100 / self.cantidad_materias, 2))

    # implementar usando modulo datetime
    def edad_ingreso(self):
        print("Edad al ingresar a la facu: ", self.edad - (datetime.now().year - self.anio))


def main():
    e = Estudiante("Damian", 21, "H", 75, 1.78, 'ISI', 2016, 36, 22)
    e.print_data()
    e.avance()
    e.edad_ingreso()


#main()
