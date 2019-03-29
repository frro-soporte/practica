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
        self.generar_dni();
    def es_mayor_edad(self):
        if self.edad>=18:
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        aleatorios = [random.randint(0,9) for _ in range(8)]
        self.dni = int(''.join(str(i) for i in aleatorios))

    def print_data(self):
        #print("El nombre es "+ self.nombre+"\nLa edad es "+self.edad+"\nEl peso es "+self.peso+"kg\nEl sexo es "+self.sexo+"\nLa altura es "+self.altura+"\nEl dni es "+self.dni)
        print(self.nombre,self.edad,self.sexo,self.peso,self.altura,self.dni)

persona = Persona("Eduardo",21,"M",75,1.75)
assert persona.es_mayor_edad()==True
