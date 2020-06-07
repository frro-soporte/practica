# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes: [Estudiante]):
    facultad = dict()
    for estudiante in estudiantes:
        if estudiante.carrera not in facultad:
            facultad[estudiante.carrera] = 1
        else:
            facultad[estudiante.carrera] = facultad[estudiante.carrera] + 1

    return facultad


test_estudiantes = [Estudiante("pedro", 24, "H", 98, 18, "Sistemas", "2018", 18, 6),
                    Estudiante("pedro", 24, "H", 98, 18, "Sistemas", "2018", 18, 6),
                    Estudiante("pedro", 24, "H", 98, 18, "mecanica", "2018", 18, 6),
                    Estudiante("pedro", 24, "H", 98, 18, "pepe", "2018", 18, 6),
                    Estudiante("pedro", 24, "H", 98, 18, "pepe", "2018", 18, 6),
                    Estudiante("pedro", 24, "H", 98, 18, "pepe", "2018", 18, 6),
                    Estudiante("pedro", 24, "H", 98, 18, "azul", "2018", 18, 6),
                    Estudiante("pedro", 24, "H", 98, 18, "Sistemas", "2018", 18, 6)]

assert organizar_estudiantes(test_estudiantes) == {'Sistemas': 3, 'mecanica': 1, 'pepe': 3, 'azul': 1}
