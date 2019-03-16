"""13. Programe una función que determine si un número entero suministrado como
argumento es primo. """

numero = 47

def primo(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print (primo(numero))
assert primo(47) == True
