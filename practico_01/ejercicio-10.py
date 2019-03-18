'''Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.'''


def mas_larga(a):
 ban=" "
 for i in a:

  if(len(i) >len(ban)  ):
   ban=i

 return ban
 pass








lista=["casa","oso","quizás"]

resultado= mas_larga(lista)

print(resultado)