# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


def organizar_estudiantes(e):
    dcarrera = {}
    x=0
    for i in e :
        if not dcarrera.get(i.carr) :
         x=0
         dcarrera.update({i.carr : x+1})
        else:
          x=dcarrera.get(i.carr)
          dcarrera.update({i.carr : x+1})
    print(dcarrera)
    return dcarrera

e = []
x = Estudiante("Ingeniería en Sistemas", 2018, 20, 10, "Fulanito", 19, 'H', 64.3, 1.72)
y = Estudiante("Ingeniería en Sistemas", 2018, 20, 10, "Cosme", 19, 'H', 64.3, 1.72)
z = Estudiante("Ingeniería Quimica", 2018, 20, 10, "Fulanito", 19, 'H', 64.3, 1.72)
w = Estudiante("Ingeniería Quimica", 2018, 20, 10, "Cosme", 19, 'H', 64.3, 1.72)
e.append(x)
e.append(y)
e.append(z)
e.append(w)

assert organizar_estudiantes(e) == {'Ingeniería en Sistemas': 2, 'Ingeniería Quimica': 2}
