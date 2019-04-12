# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

from ejercicio_03 import Persona
import datetime

class Estudiante(Persona):

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas, nombre, edad, sexo, peso, altura):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas
        

    def __repr__(self):
        return (self.nombre + " " + self.carrera)
    
    def __str__(self):
        return (self.nombre + " " + self.carrera)

    def avance(self):
        self.porcentaje = ((self.cantidad_aprobadas * 100)/ self.cantidad_materias) 
        return round(self.porcentaje, 2)
        
    # implementar usando modulo datetime
    def edad_ingreso(self):
        year = datetime.date.today().year
        self.edad_ing = self.edad - (year - self.anio)
        return self.edad_ing
    


e = Estudiante('Mecanica', 2016, 35, 24, 'juan', 21, 'M', 80, 180)
print(e.edad_ingreso())
print(e.avance())

assert e.carrera == 'Mecanica'
assert e.anio == 2016
assert e.cantidad_materias == 35
assert e.cantidad_aprobadas == 24
assert e.nombre == 'juan'
assert e.edad == 21
assert e.sexo == 'M'
assert e.peso == 80
assert e.altura == 180
assert e.edad_ingreso() == 18
assert e.avance() == 68.57