# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

import datetime, math

class Persona:

    def __init__(self,fechaNacimiento):
        self.fecha_nacimiento=datetime.datetime.strptime(fechaNacimiento,'%d/%m/%Y')

    def edad(self):
        fecha_actual=datetime.datetime.now()
        años_de_edad=(fecha_actual-self.fecha_nacimiento).days/365
        return math.trunc(años_de_edad)

persona=Persona('05/12/1996')
assert persona.edad() == 22
