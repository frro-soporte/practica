"""Practico_01 Ejercicio 5 Alumno: Pablo Uriel Alvarez Grupo 29"""
# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.
  

# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    if (letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' or letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
        return True
    else:
        return False
#Uso el assert para verificar que funcione la funcion
assert es_vocal('a')==True
assert es_vocal('A')==True
assert es_vocal('x')==False
