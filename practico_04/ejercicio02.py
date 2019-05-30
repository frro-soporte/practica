## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

from tkinter import *
from math import *
ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("250x400")
ventana.configure(background="gray")
color_boton=("gray77")


def btnClik(num):
    global operador
    operador=operador+str(num)
    entrada_txt.set(operador)
    

def clear():
    global operador
    txt = entrada_txt.get()[:-1]
    if entrada_txt.get() == 'ERROR':
        txt = ''
    entrada_txt.set(txt)
    operador=txt

def operacion():
    global operador
    try:
        resultado=str(eval(operador))
    except:
        clear()
        resultado=("ERROR")
    entrada_txt.set(resultado)
    operador = resultado


    
ancho=1
alto=1
entrada_txt=StringVar()
operador=""
clear() #MUESTRA "0" AL INICIAR LA CALCULADORA
BotonBorrar=Button(ventana,text="<",bg=color_boton,width=ancho,height=alto,command=clear).place(x=165,y=110)
Boton7=Button(ventana,text="7",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(7)).place(x=15,y=150)
Boton8=Button(ventana,text="8",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(8)).place(x=65,y=150)
Boton9=Button(ventana,text="9",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(9)).place(x=115,y=150)
BotonSuma=Button(ventana,text="+",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik("+")).place(x=165,y=150)
Boton4=Button(ventana,text="4",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(4)).place(x=15,y=200)
Boton5=Button(ventana,text="5",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(5)).place(x=65,y=200)
Boton6=Button(ventana,text="6",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(6)).place(x=115,y=200)
BotonResta=Button(ventana,text="-",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik("-")).place(x=165,y=200)
Boton1=Button(ventana,text="1",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(1)).place(x=15,y=250)
Boton2=Button(ventana,text="2",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(2)).place(x=65,y=250)
Boton3=Button(ventana,text="3",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(3)).place(x=115,y=250)
BotonDiv=Button(ventana,text="/",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik("/")).place(x=165,y=250)
Boton0=Button(ventana,text="0",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik(0)).place(x=15,y=300)
BotonResul=Button(ventana,text="=",bg=color_boton,width=8,height=alto,command=operacion).place(x=65,y=300)
BotonMulti=Button(ventana,text="*",bg=color_boton,width=ancho,height=alto,command=lambda:btnClik("*")).place(x=165,y=300)

Salida=Entry(ventana,font=('arial',20,'bold'),width=13,textvariable=entrada_txt,justify="left").place(x=10,y=60)


ventana.mainloop()