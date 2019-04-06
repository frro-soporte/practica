# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).
from datetime import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
       self.nac = nacimiento
    
    def edad(self):
        fecha = datetime.now()
        anio = fecha.year
        mes = fecha.month
        dia = fecha.day
        if mes == self.nac.month:
            if dia < self.nac.day:
                return anio - self.nac.year - 1
            else:
                return anio - self.nac.year
        elif mes < self.nac.month:
            return anio - self.nac.year - 1
        else:
            return anio - self.nac.year 


nacimiento1 = datetime.strptime("2/4/1997", '%d/%m/%Y')
nacimiento2 = datetime.strptime("3/4/1997", '%d/%m/%Y')
nacimiento3 = datetime.strptime("3/5/1997", '%d/%m/%Y')

per1 = Persona(nacimiento1)
per2 = Persona(nacimiento2)
per3 = Persona(nacimiento3)

assert per1.edad() == 22
assert per2.edad() == 22
assert per3.edad() == 21
            
