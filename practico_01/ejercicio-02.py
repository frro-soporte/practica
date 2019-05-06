# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.

a= 2
b= 4
c= 3

def mayor(a, b, c):
    if(a> b):
        if(a>c):
            return a
        else:
            return c

    elif (b>c):
        return b
    else:
        return c

assert mayor(8,4,9)==9;
assert mayor(2,5,3)==5;
assert mayor(8,3,2)==8;
assert mayor(5,6,7)==7;

