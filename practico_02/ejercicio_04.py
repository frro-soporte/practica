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

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas):
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

        Persona.__init__(self, nombre, edad, sexo, peso, altura, dni)



    def avance(self):
       print("El avance de la carrera es un: ", (self.cantidad_aprobadas/self.cantidad_materias)*100,'%')

    # implementar usando modulo datetime
    def edad_ingreso(self):
        now = datetime.now()
        dif_anio = now.year - self.anio

        print("Edad de ingreso a la carrera: ", self.edad - dif_anio)

def app():

    estudiante1 = Estudiante

    estudiante1.carrera = 'Ingenieria en sistemas de informacion'
    estudiante1.anio = 2013
    estudiante1.cantidad_materias = 40
    estudiante1.cantidad_aprobadas = 15
    estudiante1.edad = 26

    estudiante1.edad_ingreso(estudiante1)
    estudiante1.avance(estudiante1)





if __name__ == '__main__':

    app()