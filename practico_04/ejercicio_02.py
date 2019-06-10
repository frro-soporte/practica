# Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
# y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter
# que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada .
from tkinter import *
root = Tk()
root.title('Ejercicio 02')
root.geometry("280x320")

input_text = StringVar()
label = Label(root, text="CASIO").place(x=120, y=0)
Pantalla = Entry(root, textvariable=input_text,width = 35, bd = 10, insertwidth=4, bg="powder blue", justify="right").place(x=20, y =20)
var=""

def click(num):
    global var
    var = var+str(num)
    input_text.set(var)

def operacion():
    global var
    try:
        va =str(eval(var))
    except:
        clear()
        va=("ERROR")
    input_text.set(va)

def clear():
    global var
    var =("")
    input_text.set("0")

Boton0=Button(root,text="0",width=5,height=2,command=lambda:click(0)).place(x=20,y=250)
Boton1=Button(root,text="1",width=5,height=2,command=lambda:click(1)).place(x=20,y=200)
Boton2=Button(root,text="2",width=5,height=2,command=lambda:click(2)).place(x=80,y=200)
Boton3=Button(root,text="3",width=5,height=2,command=lambda:click(3)).place(x=140,y=200)
Boton4=Button(root,text="4",width=5,height=2,command=lambda:click(4)).place(x=20,y=150)
Boton5=Button(root,text="5",width=5,height=2,command=lambda:click(5)).place(x=80,y=150)
Boton6=Button(root,text="6",width=5,height=2,command=lambda:click(6)).place(x=140,y=150)
Boton7=Button(root,text="7",width=5,height=2,command=lambda:click(7)).place(x=20,y=100)
Boton8=Button(root,text="8",width=5,height=2,command=lambda:click(8)).place(x=80,y=100)
Boton9=Button(root,text="9",width=5,height=2,command=lambda:click(9)).place(x=140,y=100)
BotonSuma=Button(root,text="+",width=5,height=2,command=lambda:click("+")).place(x=200,y=100)
BotonResta=Button(root,text="-",width=5,height=2,command=lambda:click("-")).place(x=200,y=150)
BotonMulti=Button(root,text="*",width=5,height=2,command=lambda:click("*")).place(x=200,y=200)
BotonDiv=Button(root,text="/",width=5,height=2,command=lambda:click("/")).place(x=200,y=250)
BotonIgual=Button(root,text="=",width=5,height=2,command=operacion).place(x=140,y=250)
BotonCE=Button(root,text="CE",width=5,height=2, command=clear).place(x=80,y=250)




root.mainloop()