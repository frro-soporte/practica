# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).


# Probar si funciona bien importando la clase de otro ejercicio.
from datetime import datetime

#import ejercicio_03

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.generar_dni()

    def es_mayor_edad(self):
        if(self.edad >= 18 ):
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        import random
        for x in range(10):
            self.dni = random.randint(1,90)

    def print_data(self):
        resultado = "El nombre es: {}, es mayor de edad: {}, es de sexo: {}, tiene un peso de {}," \
                    " tiene una altura de {}".format(self.nombre, self.es_mayor_edad(), self.sexo, self.peso, self.altura)
        print(resultado)

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, año, cant_materias, cant_aprobadas):
        #self.nombre = nombre
        #self.edad = edad
        #self.sexo = peso
        #self.altura = altura

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
        ing = self.edad - (datetime.now().year - self.año)
#from ejercicio_03 import Persona
        return ing

es = Estudiante("Pepe", 24 , "M" ,78 ,1.75 ,"INGENIERIA EN SISTEMAS", 2013 , 25 ,20)

assert(es.avance() == 80 )

assert(es.edad_ingreso() == 18)
