# Difinir una funcion inversa() que calcule la inversion de una cadena.


def inversa(cad):
    largo = len(cad)+1
    ca2 = cad
    i = 0
    for i in range(largo):
        if i == 0:
            pass
        else:
            ca2 = ca2[:i-1] + cad[-i] + ca2[i:]
    return ca2

assert (inversa("Prueba") == 'abeurP')


