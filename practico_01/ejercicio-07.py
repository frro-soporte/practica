'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
ejemplo: es_palindromo ("radar") tendría que devolver True.'''

def es_polindromo(cad):
 reves = cad[::-1]

 if(cad==reves):

     return "True"

 else:
      return "False"


 pass

cadena = input("Ingrese la cadena de valores:")

resultado= es_polindromo(cadena)

print(resultado)