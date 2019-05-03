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

        now = datetime.datetime.now()
        nacimiento = self.nacimiento

        if ((now.month, now.day) < (nacimiento.month, nacimiento.day)):
            return (now.year - self.nacimiento.year)-1
        else:
            return now.year - self.nacimiento.year



fecha_nacimiento = datetime.datetime(1992,9,21)
persona = Persona(fecha_nacimiento)

print("La edad de la persona es: ", persona.edad())

fecha_nacimiento = datetime.datetime(1992,2,21)
persona2 = Persona(fecha_nacimiento)

assert persona.edad()==26
assert persona2.edad()==27


