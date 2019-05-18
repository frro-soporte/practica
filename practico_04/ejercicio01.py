## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Las dos líneas siguientes son necesaias para hacer
# compatible el interfaz Tkinter con los programas basados
# en versiones anteriores a la 8.5, con las más recientes.

# !/usr/bin/env python
# -*- coding: utf-8 -*-


from tkinter import *
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x150")

valor_1 = StringVar()
valor_2 = StringVar()
resultado = StringVar()
label1 =Label(ventana,  text ="1er Valor").place(x=10, y=10)
#label1.grid(row =1, column =0)

num1_txtbx =Entry(ventana, textvariable=valor_1, width=5).place(x=100, y=10)
# num1_txtbx.grid(row =1, column =1)

label2 =Label(ventana, text ="2do Valor").place(x=10, y=50)

num2_txtbx =Entry(ventana, textvariable=valor_2,width=5).place(x=100, y=50)

def suma():
    
    if (valor_1.get() and valor_2.get() != ""):
        try:
            num1 =float(valor_1.get())
            num2 =float(valor_2.get())
            answer = 'Resultado:', num1 + num2
            resultado.set(answer)
            valor_1.set('')            
            valor_2.set('')

        except:
            resultado.set("Entrada invalida, vuelva a intentarlo")
    else:
        resultado.set("Se deben llenar todos los campos")


def resta():
    if (valor_1.get() and valor_2.get() != ""):
        try:
            num1 = float(valor_1.get())
            num2 = float(valor_2.get())
            answer = 'Resultado:', num1 - num2
            resultado.set(answer)
            valor_1.set('')            
            valor_2.set('')

        except:
            resultado.set("Entrada invalida, vuelva a intentarlo")
    else:
        resultado.set("Se deben llenar todos los campos")


def multiplicacion():
    if (valor_1.get() and valor_2.get() != ""):
        try:
            num1 = float(valor_1.get())
            num2 = float(valor_2.get())
            answer = 'Resultado:', num1 * num2
            resultado.set(answer)
            valor_1.set('')            
            valor_2.set('')

        except:
            resultado.set("Entrada invalida, vuelva a intentarlo")
    else:
        resultado.set("Se deben llenar todos los campos")


def division():
    if (valor_1.get() and valor_2.get() != ""):

        try:
            num1 = float(valor_1.get())
            num2 = float(valor_2.get())
            answer = 'Resultado:', num1 / num2
            resultado.set(answer)
            valor_1.set('')            
            valor_2.set('')

        except:
            resultado.set("Entrada invalida, vuelva a intentarlo")
    else:
        resultado.set("Se deben llenar todos los campos")

ancho_boton = 1
alto_boton = 1

suma =Button(ventana, text="+",width=ancho_boton, height=alto_boton, command= suma).place(x=170, y=10)
resta=Button(ventana, text="-", width=ancho_boton, height=alto_boton,command= resta).place(x=220, y=10)
multi=Button(ventana, text="x",width=ancho_boton, height=alto_boton, command= multiplicacion).place(x=170, y=45)
division=Button(ventana, text="%",width=ancho_boton, height=alto_boton, command= division).place(x=220, y=45)

# salida = Entry(ventana,textvariable=resultado, justify='center').place(x=50,y=100)
salida2 = Label(ventana, textvariable=resultado, justify='center').place(x=50,y=100)

ventana.mainloop()
