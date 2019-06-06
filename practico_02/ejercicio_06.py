# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).


from datetime import datetime, date, timedelta


class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nac = datetime.strptime(nacimiento,"%d %B- %Y")

    def edad(self):
        hoy = datetime.now()
        #print(hoy)
        #print(self.nac)
        diferencia = hoy - self.nac
        print("Edad:", int(float(diferencia.days)/365.2))

j = Persona('11 April- 1996')
j.edad()

