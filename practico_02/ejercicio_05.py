# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from ejercicio_04 import Estudiante

def organizar_estudiantes(est : list[Estudiante]):
    c = []
    dicc = {}

    for i in est :
        if (i.c not in Estudiante.carrera):
            c.append(i.Estudiante.carrera)
    for z in c :
        aux = 0
        for k in est:
            if (k.Estudiante.carrera == z):
                aux =+ 1
                dicc[k.Estudiante.carrera] = aux
    return dicc


#listAlu = []
#Alu1 = Estudiante("Pepito",35,"M",75.5,1.65, "Ingenieria en sistemas",2013,20,2)
#Alu2 = Estudiante("Juan",22,"M",70,1.65,"Ingenieria Quimica",2015,25,20)
#Alu3 = Estudiante("Jorge",20,"M",90,1.60,"Ingenieria Mecanica",2013,38,35)
#listAlu = [Alu1,Alu2,Alu3]



