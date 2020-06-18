# Programe una clase EJERCICIO tiene los siguientes métodos : INICIO se le pasa una fecha y
# devuelve el 1 de Julio anterior . FIN se le pasa una fecha y devuelve el 30 de Junio próximo ,
# SEMANA devuelve el nro de semana contando a partir del 1 de Julio anterior .
import datetime as dt


class Ejercicio:

    @staticmethod
    def Inicio(fecha):
        f = "01/07/"
        if fecha.month >= 7:
            if fecha.month == 7 & fecha.day == 1:
                f += str(fecha.year - 1)
            else:
                f += str(fecha.year)
        else:
            f += str(fecha.year - 1)
        return f

    @staticmethod
    def Fin(fecha):
        f = "30/06/"
        if fecha.month <= 6:
            if fecha.month == 6 & fecha.day == 30:
                f += str(fecha.year + 1)
            else:
                f += str(fecha.year)
        else:
            f += str(fecha.year + 1)
        return f

    @staticmethod
    def Semana(fecha):
        # la cantidad de semanas hasta 01/07 es 26
        if fecha.month >= 7:
            semanas = dt.date(fecha.year, fecha.month, fecha.day).isocalendar()[1] - 26
        else:
            semanas = dt.date(fecha.year, fecha.month, fecha.day).isocalendar()[1] + 26
        return semanas


def main():
    f1 = '24/06/2017'
    # f1 = '01/02/2017'
    f1 = dt.datetime.strptime(f1, '%d/%m/%Y')
    f2 = '22/11/2017'
    f2 = dt.datetime.strptime(f2, '%d/%m/%Y')

    print("Fecha: ", f1)
    print("1/7 anterior: ", Ejercicio.Inicio(f1))
    print("30/06 proximo", Ejercicio.Fin(f1))
    print("Cantidad de semanas desde 1/07 anterior: ", Ejercicio.Semana(f1))
    print()
    print("Fecha: ", f2)
    print("1/7 anterior: ", Ejercicio.Inicio(f2))
    print("30/06 proximo", Ejercicio.Fin(f2))
    print("Cantidad de semanas desde 1/07 anterior: ", Ejercicio.Semana(f2))


main()
