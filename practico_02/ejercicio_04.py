# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).
from _datetime import datetime
from datetime import date
from practico_02.ejercicio_03 import Persona


class Estudiante(Persona):

    def __init__(self,nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        super(Estudiante,self).__init__(nombre, edad, sexo, peso, altura)
        self.carrera=carrera
        self.anio=anio
        self.cantidad_materias=cantidad_materias
        self.cantidad_aprobadas=cantidad_aprobadas


    pass

    def avance(self):
           return (self.cantidad_aprobadas/self.cantidad_materias)*100

    pass

    # implementar usando modulo datetime
    def edad_ingreso(self):
        x = datetime.now()
        "x=date.today()"
        return self.edad-(x.year-self.anio)
pass

est=Estudiante("Jose", 24,"Masculino", 80, 1.85,"Ingeniería en sistemas", 2013, 41, 30)

print("Avance de la carrera: ",est.avance())
print("Edad actual: ",est.edad_ingreso())

assert est.avance()==73.17073170731707
assert est.edad_ingreso()==18