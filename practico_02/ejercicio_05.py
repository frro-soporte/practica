# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


class _IteradorListaEnlazada(Estudiante):
    " Iterador para la clase ListaEnlazada "
    def __init__(self, prim):
        """ Constructor del iterador.
            prim es el primer elemento de la lista. """
        self.actual = prim


def organizar_estudiantes(estudiantes):
    carreras = {'ISI':0, 'IM':0, 'IE':0, 'IQ':0}

    for estudiante in estudiantes:
        if estudiante.carrera in carreras:
            carreras[estudiante.carrera] += 1

    return carreras


def app():

    listaEstudiantes = []

    e1 = Estudiante('Nahuel', 26, 'H', 90, 174, '', 'ISI', 2013, 40, 15)
    e2 = Estudiante('David', 26, 'H', 90, 174, '', 'ISI', 2013, 40, 15)
    e3 = Estudiante('Ernesto', 26, 'H', 90, 174, '', 'IM', 2013, 40, 15)
    e4 = Estudiante('Elene', 26, 'H', 90, 174, '', 'IQ', 2013, 40, 15)

    listaEstudiantes.append(e1)
    listaEstudiantes.append(e2)
    listaEstudiantes.append(e3)
    listaEstudiantes.append(e4)

    print(organizar_estudiantes(listaEstudiantes))

    assert organizar_estudiantes(listaEstudiantes) == {'ISI': 2, 'IM': 1, 'IE': 0, 'IQ': 1}

if __name__ == '__main__':
    app()
