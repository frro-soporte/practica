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


# Probar si funciona bien importando la clase de otro ejercicio.

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, año, cant_materias, cant_aprobadas):
        Persona.__init__(self,nombre,edad,sexo,peso,altura)
        self.carrera = carrera
        self.año = año
        self.cant_materias = cant_materias
        self.cant_aprobadas = cant_aprobadas
        pass

    def avance(self):

        porc = round(self.cant_aprobadas*100/self.cant_materias)
        return porc

    # implementar usando modulo datetime
    def edad_ingreso(self):
        ing = self.edad - (datetime.datetime.now().year - self.año)
        return ing

es = Estudiante("Pepe", 24 , "M" ,78 ,1.75 ,"INGENIERIA EN SISTEMAS", 2013 , 25 ,20)

assert(es.avance() == 80 )

assert(es.edad_ingreso() == 18)
