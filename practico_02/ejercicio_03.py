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

    def __init__(self, nombre, edad, sexo, peso, altura, dni):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = dni

    def es_mayor_edad(self):

        if self.edad >= 18:
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        for i in range (8):
            self.dni += str(randint(0,9))
        return self.dni

    def print_data(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Sexo: ", self.sexo)
        print("Peso: ", self.peso)
        print("Altura: ", self.altura)
        print("DNI: ", self.dni)

def app():

    alumno1 = Persona

    alumno1.nombre = 'Nahuel'
    alumno1.edad = 26
    alumno1.sexo = 'H'
    alumno1.peso = 90
    alumno1.altura = 1.75
    alumno1.dni = ''

    alumno1.es_mayor_edad(alumno1)
    alumno1.generar_dni(alumno1)
    alumno1.print_data(alumno1)




if __name__ == '__main__':

    app()