'''Programe una función que determine si un número entero suministrado como
argumento es primo.'''
def primo(a):
    if a < 1:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
    return True

a= 7
assert primo(a)== True
