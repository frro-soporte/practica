## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

import tkinter
from tkinter import *
def suma():
    x=int(textbox1.get())+int(textbox2.get())
    print(x)
    salida["text"]=x

def suma():
    x=int(textbox1.get())+int(textbox2.get())
    print(x)
    salida["text"]=x

def resta():
    x=int(textbox1.get())-int(textbox2.get())
    print(x)
    salida["text"]=x

def multiplicacion():
    x=int(textbox1.get())*int(textbox2.get())
    print(x)
    salida["text"]=x

def division():
    x=int(textbox1.get())/int(textbox2.get())
    print(x)
    salida["text"]="Resultado:"+x

ventana=tkinter.Tk()
ventana.title("Calculadora")
ventana.geometry("300x310")
pr= tkinter.Label(ventana,text="Primer Operando")
textbox1= tkinter.Entry(ventana)
se= tkinter.Label(ventana,text="Segundo Operando")
textbox2= tkinter.Entry(ventana)
z= tkinter.Label(ventana,text="")
boton1= tkinter.Button(ventana,text="Suma +", command=suma)
boton2= tkinter.Button(ventana,text="Resta -", command=resta)
boton4= tkinter.Button(ventana,text="Multiplicación *", command=multiplicacion)
boton3= tkinter.Button(ventana,text="División /", command=division)
a= tkinter.Label(ventana,text="")
salida= tkinter.Label(ventana,text="")
d= tkinter.Label(ventana,text="")


d.pack()
pr.pack()
textbox1.pack()
se.pack()
textbox2.pack()
z.pack()
boton1.pack()
boton2.pack()
boton4.pack()
boton3.pack()
a.pack()
salida.pack()
ventana.mainloop()
