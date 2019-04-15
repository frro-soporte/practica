# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
	def __init__(self, nacimiento):
		self.nacimiento = nacimiento

	def edad(self):
		delta = datetime.datetime.now() - self.nacimiento
		return delta.days//365

assert(Persona(datetime.datetime(1998,6,2)).edad() == 20)
