## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

from tkinter import *

raiz = Tk()
raiz.title("Calculadora")
raiz.geometry("400x100")
raiz.configure(bg = 'beige')
color_boton=("gray77")

v1 = StringVar()
v2 = StringVar()
resultado = StringVar()
label1 =Label(raiz,  text ="Primer Operando").place(x=40, y=10)
v1_txt =Entry(raiz, textvariable=v1, width=5).place(x=70, y=40)
label2 =Label(raiz, text ="Segundo Operando").place(x=180, y=10)
v2_txt =Entry(raiz, textvariable=v2,width=5).place(x=210, y=40)

def operar(opcion):
    if (v1.get() and v2.get() != ""):
        try:
            num1 =float(v1.get())
            num2 =float(v2.get())
            answer = 'El resultado es: ' + str(eval(v1.get()+opcion+v2.get()))
            resultado.set(answer)
            v1.set('')
            v2.set('')
        except:
            resultado.set("Ingreso invalido")
    else:
        resultado.set("Ingrese todos los datos")

def suma():
    opcion='+'
    operar(opcion)

def resta():
    opcion='-'
    operar(opcion)

def multiplicacion():
    opcion='*'
    operar(opcion)

def division():
    opcion = '/'
    operar (opcion)

suma =Button(raiz, text="+",width=1,bg=color_boton, height=1, command= suma).place(x=310, y=40)
resta=Button(raiz, text="-", width=1, bg=color_boton, height=1,command= resta).place(x=330, y=40)
multi=Button(raiz, text="x",width=1, bg=color_boton, height=1, command= multiplicacion).place(x=350, y=40)
division=Button(raiz, text="%",width=1, bg=color_boton, height=1, command= division).place(x=370, y=40)
salida = Label(raiz, textvariable=resultado, justify='center').place(x=40,y=70)

raiz.mainloop()

