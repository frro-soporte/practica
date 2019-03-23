# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    if (numero>=1):
        resultado=False
        if(numero==1 or numero==2):
            return True

        else:
            if((numero % 2)!=0):
                if(numero%3 !=0):
                    if (numero % 5 != 0):
                        if (numero % 7 != 0):

                            if (numero % 11 != 0):
                                return True
                            else:
                                if(numero==11):
                                    return True
                        else:
                            if(numero==7):
                                return True

                    else:
                        if (numero == 5):
                            return True
                else:
                    if(numero==3):
                        return True

            return resultado



    else:
        print('Ingresaste un numero menor que 1')



assert es_primo(3) == True;
assert es_primo(113) == True;
assert es_primo(4) == False;


