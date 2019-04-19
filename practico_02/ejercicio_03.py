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

#try:
nombre = input('Ingresar nombre')
edad = int(input('Ingresar edad'))
sexo = input('Ingresar sexo M\F')
peso = float(input('Ingresar peso'))
altura = float(input('Ingresar altura'))
p = Persona(nombre, edad, sexo, peso, altura)
print(p.print_data())

#except ValueError:
 #   print('Ingreso datos erroneos, intente nuevamente')
