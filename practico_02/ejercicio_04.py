# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

from practico_02.ejercicio_03b import Persona
from datetime import datetime 

class Estudiante(Persona):

    def __init__(self, nombre, edad, carrera, anio, cantidad_materias, cantidad_aprobadas):
        super().__init__(nombre, edad)
        
        self.per_edad = edad
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        avance = round((self.cantidad_aprobadas/self.cantidad_materias) * 100,2)
        return avance
    # implementar usando modulo datetime
    def edad_ingreso(self):
        edad = self.per_edad - (datetime.now().year - self.anio)
        return edad
    
alumno = Estudiante("Juan", 25,"Ing en sistemas", 2012, 30, 10);
assert(alumno.edad_ingreso())==18;
assert(alumno.avance()) == 33.33;

