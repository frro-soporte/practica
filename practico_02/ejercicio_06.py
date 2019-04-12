# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from datetime import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.fecha = datetime.strptime(nacimiento, '%d/%m/%Y')
        self.edad = self.calcula_edad()

    def calcula_edad(self):
        anio_actual = datetime.now()
        edad = anio_actual.year - self.fecha.year
        return edad

nacimiento = '19/03/1998'
a = Persona(nacimiento)
print('La persona tiene ', a.edad, ' años de edad.')

assert a.calcula_edad() == 21


