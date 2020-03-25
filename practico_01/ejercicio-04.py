# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor(grados):
    
    try: 

        grados = float(input('Ingrese la cantidad de Grados Celsius a transformar en Fahrenheit: '))

        f = 9 / 5 * grados + 32

        print(grados, ' grados Celsius equivalen a ', f, 'grados Fahrenheit.')

    except: 

        print("Los grados deben ser numeros.")


