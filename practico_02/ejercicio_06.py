# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).
from datetime import datetime


class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento: str):
        self.nacimiento = datetime.strptime(nacimiento, "%d/%m/%Y")

    def edad(self):
        if datetime.now() < self.nacimiento:
            return "fecha incorrecta"
        edad = datetime.now().year - self.nacimiento.year
        if edad == 0:
            return "Nacio hoy"
        if edad == 1:
            if datetime.now().month <= self.nacimiento.month:
                if datetime.now().day < self.nacimiento.day:
                    return "{0} dias".format((datetime.now() - self.nacimiento).days)
            return "{0} año".format(edad)
        if datetime.now().month < self.nacimiento.month:
            return "{0} año".format(edad - 1) if (edad - 1) == 1 else "{0} años".format(edad - 1)
        if datetime.now().month > self.nacimiento.month:
            return "{0} año".format(edad) if edad == 1 else "{0} años".format(edad)
        if datetime.now().day < self.nacimiento.day:
            return "{0} año".format(edad - 1) if (edad - 1) == 1 else "{0} años".format(edad - 1)
        return "{0} año".format(edad) if edad == 1 else "{0} años".format(edad)


#testeado el 21 de marzo de 2020
assert Persona("21/03/2020").edad() == "Nacio hoy"
assert Persona("21/03/2019").edad() == "1 año"
assert Persona("22/03/2019").edad() == "365 dias"
assert Persona("24/03/2019").edad() == "363 dias"
assert Persona("20/03/2019").edad() == "1 año"
assert Persona("22/03/2018").edad() == "1 año"
assert Persona("20/03/2018").edad() == "2 años"
assert Persona("05/07/1997").edad() == "22 años"

