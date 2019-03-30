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

    def generar_dni(self):
        d=random.randint(00000000,99999999)
        return d

    def __init__(self,nombre,edad,sexo,peso,altura):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.peso=peso
        self.altura=altura
        self.dni=self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def print_data(self):
        print('Nombre:',self.nombre)
        print('Edad:',self.edad)
        print('Sexo:',self.sexo)
        print('Peso:',self.peso,'Kg')
        print('Altura:',self.altura,'m')
        print('DNI:',self.dni)

persona=Persona('Agustin Yurescia',22,'H',79.6,1.70)
assert persona.es_mayor_edad() == True

