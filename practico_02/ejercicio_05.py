from practico_02.ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
    isi=iq=ic=ie=0
    for record in estudiantes:
        if(record.carrera=='Ing en sistemas'):
            isi +=1
        if(record.carrera=='Ing Quimica'):
            iq +=1
        if(record.carrera=='Ing Civil'):
            ic +=1
        if(record.carrera=='Ing Electrica'):
            ie +=1
    dict = {'ISI': isi, 'IQ': iq, 'IC': ic, 'IE': ie}
    return dict

uno = Estudiante("Juan", 25,"Ing en sistemas", 2012, 30, 10)
dos = Estudiante("Juan", 25,"Ing Civil", 2012, 30, 10)
tres = Estudiante("Juan", 25,"Ing Quimica", 2012, 30, 10) 
cuatro = Estudiante("Juan", 25,"Ing Electrica", 2012, 30, 10) 
cinco = Estudiante("Juan", 25,"Ing Quimica", 2012, 30, 10) 
seis = Estudiante("Juan", 25,"Ing en sistemas", 2012, 30, 10) 
siete = Estudiante("Juan", 25,"Ing en sistemas", 2012, 30, 10)
lista = [uno, dos, tres, cuatro, cinco, seis, siete]
assert(organizar_estudiantes(lista)) == {'ISI': 3, 'IQ': 2, 'IC': 1, 'IE': 1}

