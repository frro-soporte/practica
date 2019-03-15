def lista_numeros():
    op = ""
    numeros = []

    while op.lower() != "fin":
        op = input("Introduzca un número: ")

        if op.isnumeric():
            numeros.append(int(op))
 
    return f"Maximo: {reduce(max, numeros)}" "\n" f"Minimo: {min(numeros)}"
    
# Los casos de prueban deben comprobarse con la consola