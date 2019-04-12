# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.
import random

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_edad(self):
        if(self.edad>=18):
            print('La persona es mayor de edad \n')
            return True
        else:
            print('La persona es menor de edad \n')
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        dni = random.randint(37000000, 80000000)
        return dni
    def print_data(self):
        print(  '\n Nombre:', self.nombre, '\n',
                'Dni:' ,self.dni, '\n',
                'Edad:',self.edad, '\n',
                'Sexo:',self.sexo, '\n',
                'Peso:',self.peso, 'kg','\n',
                'Altura:',self.altura, 'mts', '\n')

