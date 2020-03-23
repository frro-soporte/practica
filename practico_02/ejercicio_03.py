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
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.peso=peso
        self.altura=altura
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        if self.edad>=18:
            return True
        else:
            return False


    # llamarlo desde __init__
    def generar_dni(self):
        dni = random.randint(1000000, 50000000)
        return dni

    def print_data(self):
        print("DNI:", self.dni)
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("Peso:", self.peso,"Kg")
        print("Altura:", self.altura,"m")


a=Persona("Damian",21,"H",75,1.78)
print("Es mayor de edad?", a.es_mayor_edad())
a.print_data()

