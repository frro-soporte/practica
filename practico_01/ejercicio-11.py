# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(num):
    z=False
    if num > 1:
     for i in range(2,num):
         if (num % i) == 0:
             z=False
             return z
             break
         else:
          z=True
          return z
    else :
        return z


assert es_primo(4) == False
assert es_primo(7) == True

