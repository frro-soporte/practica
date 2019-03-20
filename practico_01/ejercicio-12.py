def suma(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    return sum


n = input("Ingrese el numero N (no negativo)")
assert suma(int(n)) == 10

