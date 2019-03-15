# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def length(xs):
    return len(xs)

def length_2(xs):
    return sum(1 for i in xs)

def all_test(func):

    # Case for empty list
    assert func([]) == 0

    # Case for non-empty list
    assert func([1, 2, 3]) == 3

all_test(length)
all_test(length_2)