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


    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def es_mayor_edad(self):
        if self.edad > 18:
            print("Es mayor de edad ")
            return True
        else:
            print('No es mayor de edad ')
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        dni = ''
        for i in range(8):
            dni = dni + random.randint(0, 10).__str__()
        print(dni)
        return

    def print_data(self):
        print('El nombre es: ', self.nombre)
        print('La edad es: ', self.edad)
        print('El sexo es: ', self.sexo)
        print('El peso es: ', self.peso)
        print('La altura es: ', self.altura)


a=Persona('pato', 23, 'M', 84, 1.85)
a.generar_dni()
a.es_mayor_edad()
a.print_data()
