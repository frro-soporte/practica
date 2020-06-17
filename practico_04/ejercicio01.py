## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .
from tkinter import *
from tkinter import ttk, font

def suma():
    res = v1.get() + v2.get()
    lbl.configure(text= res)

def resta():
    res = v1.get() - v2.get()
    lbl.configure(text= res)

def multip():
    res = v1.get() * v2.get()
    lbl.configure(text= res)

def divis():
    if v2.get() != 0:
        res = v1.get() / v2.get()
        lbl.configure(text= res)
    else:
        lbl.configure(text= 'No se puede dividir por 0')

window = Tk()

marco = ttk.Frame(window, borderwidth=2, relief="raised", padding=(10,10))
v1 = IntVar()
v2 = IntVar()

marco.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = (N, S, E, W))

window.title("Calculadora")

lbl = Label(marco, text="")

lbl.grid(column=1, row=16)

e1 = Entry(marco, width=10, textvariable = v1)
e2 = Entry(marco, width=10, textvariable = v2)

e1.grid(column=0, row=3,padx = 5, pady = 5, sticky = (E, W))
e2.grid(column=2, row=3,padx = 5, pady = 5, sticky = (E, W))

suma = Button(marco, text="+", command=suma)
resta = Button(marco, text="-", command=resta)
mult = Button(marco, text="x", command=multip)
div = Button(marco, text="/", command=divis)

suma.grid(column=1, row=0,padx = 5, pady = 5, sticky = ( E, W))
resta.grid(column=1, row=3,padx = 5, pady = 5, sticky = ( E, W))
mult.grid(column=1, row=6,padx = 5, pady = 5, sticky = ( E, W))
div.grid(column=1, row=9,padx = 5, pady = 5, sticky = ( E, W))

window.mainloop()
