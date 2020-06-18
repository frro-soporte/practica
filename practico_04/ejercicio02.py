## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada .

from tkinter import *
ventana = Tk()
ventana.title('Calculadora')

salida = StringVar()
Pantalla = Entry(ventana, textvariable=salida, width=40).grid(column = 0,row=0, columnspan=4)
var=""

def click(num):
    global var
    var = var+str(num)
    salida.set(var)

def operacion():
    global var
    try:
        va =str(eval(var))
    except:
        borrar()
        va=("Error")
    salida.set(va)

def borrar():
    global var
    var =("")
    salida.set("0")


ancho=8
altura=3

Boton1=Button(ventana,text="1",width=ancho,height=altura,command=lambda:click(1)).grid(column = 0,row=3)
Boton2=Button(ventana,text="2",width=ancho,height=altura,command=lambda:click(2)).grid(column = 1,row=3)
Boton3=Button(ventana,text="3",width=ancho,height=altura,command=lambda:click(3)).grid(column = 2,row=3)
Boton4=Button(ventana,text="4",width=ancho,height=altura,command=lambda:click(4)).grid(column = 0,row=2)
Boton5=Button(ventana,text="5",width=ancho,height=altura,command=lambda:click(5)).grid(column = 1,row=2)
Boton6=Button(ventana,text="6",width=ancho,height=altura,command=lambda:click(6)).grid(column = 2,row=2)
Boton7=Button(ventana,text="7",width=ancho,height=altura,command=lambda:click(7)).grid(column = 0,row=1)
Boton8=Button(ventana,text="8",width=ancho,height=altura,command=lambda:click(8)).grid(column = 1,row=1)
Boton9=Button(ventana,text="9",width=ancho,height=altura,command=lambda:click(9)).grid(column = 2,row=1)
Boton0=Button(ventana,text="0",width=ancho,height=altura,command=lambda:click(0)).grid(column = 1,row=4)
BotonSuma=Button(ventana,text="+",width=ancho,height=altura,command=lambda:click("+")).grid(column =3,row=1)
BotonResta=Button(ventana,text="-",width=ancho,height=altura,command=lambda:click("-")).grid(column = 3,row=2)
BotonMulti=Button(ventana,text="*",width=ancho,height=altura,command=lambda:click("*")).grid(column = 3,row=3)
BotonDiv=Button(ventana,text="/",width=ancho,height=altura,command=lambda:click("/")).grid(column = 3,row=4)
BotonIgual=Button(ventana,text="=",width=ancho,height=altura,command=operacion).grid(column = 2,row=4)
BotonCE=Button(ventana,text="CE",width=ancho,height=altura, command=borrar).grid(column = 0,row=4)




ventana.mainloop()
