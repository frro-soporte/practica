#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
#cadena "estoy probando" debería devolver la cadena "odnaborp yotse".

def inversa(cad):
    invertcad=[]
    invertcad=cad[::-1]
    return invertcad

print(inversa("hola mundo"))
assert(inversa("hola mundo")=="odnum aloh")
