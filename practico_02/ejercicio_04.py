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

    def __init__(self, nombre, edad, sexo, peso, altura, dni, carrera='', anio=None, cantidad_materias=None, cantidad_aprobadas=None):
        self.nombre=nombre
        self.sexo = sexo
        self.altura = altura
        self.dni = dni
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas


        Persona.__init__(self, nombre, edad, sexo, peso, altura, dni)


    def avance(self):
       return self.cantidad_aprobadas/self.cantidad_materias*100

    # implementar usando modulo datetime
    def edad_ingreso(self):
        now = datetime.now()
        dif_anio = now.year - self.anio

        return self.edad - dif_anio

def app():
    e1 = Estudiante('Nahuel',26,'H',90,174,'','ISI',2013,40,15)

    print("Edad de ingreso a la carrera: ", e1.edad_ingreso())
    print( "El avance de la carrera es un: ", e1.avance(),"%")

    assert e1.edad_ingreso() == 20
    assert e1.avance() == 37.5

if __name__ == '__main__':

    app()