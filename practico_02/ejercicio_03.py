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
        self.nom=nombre
        self.ed=edad
        self.se=sexo
        self.pe=peso
        self.al=altura
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        a =  self.ed > 18
        return a

    # llamarlo desde __init__
    def generar_dni(self):
        doc = random.randrange(10000000, 99999999)
        return doc


    def print_data(self):
        print( self.nom,self.ed,self.se,self.al,self.dni)


algo = Persona ('juan',27,'H',89,1.87)
assert ((algo.es_mayor_edad())==True)
algo.print_data()
