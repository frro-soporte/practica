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
        fechaHoy = datetime.datetime.now()
        posibleEdad = fechaHoy.year - self.nacimiento.year
        #obtengo la diferencia entre fechas para determinar la posible edad , despues lo voy a ir comparando con los meses

        ## primero me fijo que si ya los cumplio y sino le resto uno
            # no lo cumplio todavia
        if fechaHoy.month < self.nacimiento.month:
                return posibleEdad - 1
            #ya lo cumplio
        if fechaHoy.month > self.nacimiento.month:
                return posibleEdad
            #esta en le mes pero..
        elif fechaHoy.month == self.nacimiento.month:
                ## no los cumplio
            if fechaHoy.day < self.nacimiento.day:
                    return posibleEdad -1
                ## ya lo cumplio
            elif fechaHoy.day > self.nacimiento.day:
                    return posibleEdad
                ## feliz cumpleaños
            elif fechaHoy.day == self.nacimiento.day:
                    return posibleEdad


c = Persona(datetime.date(1995,5,15))
assert(c.edad() == 23)



