# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

import datetime
from ejercicio_03 import Persona

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cm = cantidad_materias
        self.ca = cantidad_aprobadas

    def avance(self):
        av = (self.ca * 100)/self.cm
        return int(av)

    # implementar usando modulo datetime
    def edad_ingreso(self):
        n = int(datetime.datetime.today().strftime('%Y'))
        return self.age - (n-self.anio)

p = Estudiante('Juan', 23, 'Masculino', 66, 1.64, 'isi', 2013, 12, 9)
print('El procentaje aprobado es de:', p.avance())
assert (p.edad_ingreso() == 17)
assert (p.avance() == 75)

