# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante

def organizar_estudiantes(estudiantes):
    diccionario={}
    isi=0
    mec=0
    civ=0
    for i in estudiantes[:]:
        if i.carrera == 'ISI':
            isi=isi+1
        elif i.carrera == 'MEC':
            mec=mec+1
        elif i.carrera == 'CIVIL':
            civ=civ+1
    diccionario['ISI']=isi
    diccionario['MECANICA']=mec
    diccionario['CIVIL']=civ
    print(diccionario)

estudiantes=[]
resp='SI'
while resp == 'SI' or resp == 'si':
    carrera=input('Ingrese la carrera del alumno (ISI - MEC - CIVIL): ')
    est=Estudiante('',0,'',0,0,'',carrera,0,0,0)
    estudiantes.append(est)
    resp=input('\nOtra?')
organizar_estudiantes(estudiantes)
