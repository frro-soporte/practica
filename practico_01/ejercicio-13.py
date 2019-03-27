#Programe una función que determine si un número entero suministrado como
#argumento es primo.

def esprimo(num):
     for i in range(2,num):
        if (num%i==0):
            return False
        else:
            return True


if(esprimo(33)):
    print("el numero es primo")
else:
    print("el numero no es primo")
assert(esprimo(33)==True)
