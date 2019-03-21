'''Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.'''


def mas_larga(a):
 ban=" "
 for i in a:

  if(len(i) >len(ban)  ):
   ban=i

 return ban
 pass




assert mas_larga(['oso','casa','astronomia'])=='astronomia'
assert mas_larga(['oso','casa','pie'])=='casa'