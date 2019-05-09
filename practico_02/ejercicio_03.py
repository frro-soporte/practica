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
from random import randint


class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):

        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    pass

    def es_mayor_edad(self):

        if (self.edad < 18):
            return False
        else:

            return True

    def generar_dni(self):

        numeros = []
        for x in range(8):
            a = randint(0, 9)
            numeros.append(str(a))

        dni = ''
        for x in range(8):
            dni = dni + numeros[x]

        return (dni)

    def print_data(self):

        return self.nombre, self.edad, self.sexo, self.peso, self.altura


per = Persona("catriel", 20, 80, 1.85, "masculino")

print("Datos de la persona: ", per.print_data())
print("Es mayor de edad: ", per.es_mayor_edad())
print("El dni es: ", per.generar_dni())

assert per.es_mayor_edad() == True
assert per.print_data() == ('catriel', 20, 80, 1.85, 'masculino')