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
        self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True

    # llamarlo desde __init__
    def generar_dni(self):
        aleatorios = [random.randint(0,9) for _ in range(8)]
        self.dni = int(''.join(str(i) for i in aleatorios))

    def print_data(self):
        print("Nombre: {} , Edad: {}, Sexo: {}, Peso: {}, Altura: {}, Dni: {} ".format(self.nombre,self.edad,self.sexo,self.peso,self.altura,self.dni))

assert Persona('Joaquin',23,'M',67,1.67).es_mayor_edad() == True
Persona('Joaquin',23,'M',67,1.67).print_data()
