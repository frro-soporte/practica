## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

from tkinter import *
from math import *

raiz=Tk()
raiz.title("Calculadora")
raiz.geometry("250x400")
raiz.configure(bg="beige")
color_boton=("gray77")

def btnClik(num):
    global operador
    operador=operador+str(num)
    entrada_txt.set(operador)

def clear():
    global operador
    txt = entrada_txt.get()[:-1]
    if entrada_txt.get() == 'Error':
        txt = ''
    entrada_txt.set(txt)
    operador=txt

def operacion():
    global operador
    try:
        resultado=str(eval(operador))
    except:
        clear()
        resultado=("Error")
    entrada_txt.set(resultado)
    operador = resultado

ancho=3
alto=1
entrada_txt=StringVar()
operador=""
clear()

Boton7=Button(raiz,text="7",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(7)).place(x=15,y=150)
Boton8=Button(raiz,text="8",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(8)).place(x=65,y=150)
Boton9=Button(raiz,text="9",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(9)).place(x=115,y=150)
BotonSuma=Button(raiz,text="+",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik("+")).place(x=165,y=150)
Boton4=Button(raiz,text="4",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(4)).place(x=15,y=200)
Boton5=Button(raiz,text="5",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(5)).place(x=65,y=200)
Boton6=Button(raiz,text="6",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(6)).place(x=115,y=200)
BotonResta=Button(raiz,text="-",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik("-")).place(x=165,y=200)
Boton1=Button(raiz,text="1",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(1)).place(x=15,y=250)
Boton2=Button(raiz,text="2",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(2)).place(x=65,y=250)
Boton3=Button(raiz,text="3",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(3)).place(x=115,y=250)
BotonDiv=Button(raiz,text="/",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik("/")).place(x=165,y=250)
Boton0=Button(raiz,text="0",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(0)).place(x=15,y=300)
BotonResul=Button(raiz,text="=",bg=color_boton,width=10,height=alto,command=operacion).place(x=65,y=300)
BotonMulti=Button(raiz,text="x",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik("*")).place(x=165,y=300)

Salida=Entry(raiz,font=('arial',20,'bold'),width=13,textvariable=entrada_txt,justify="left").place(x=10,y=60)

raiz.mainloop()
