#1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
# Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
# al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

from tkinter import *
root = Tk()
root.title('Ejercicio 01')
root.geometry("300x200")


def close_window():
    root.destroy()
    root.quit()


root.protocol("WM_DELETE_WINDOW", close_window)
input_text = StringVar()
salida = Entry(root, textvariable=input_text,width = 40, bd = 10, insertwidth=4, bg="powder blue", justify="right").place(x=10, y =140)

label1 = Label(root, text="Primer Operador").place(x=10, y=10)
label2 = Label(root, text="Segundo Operador").place(x=10, y=40)
var1 = DoubleVar()
var1.set('')
var2 = DoubleVar()
var2.set('')


input1 = Entry(root,textvariable = var1).place(x=150, y = 10)
input2 = Entry(root,textvariable = var2).place(x=150, y = 40)

button_suma = Button(root, text="+", width= 5, height= 3, command=lambda:suma() ).place(x=40, y = 70)
button_resta = Button(root, text="-", width= 5, height= 3,command=lambda:resta()).place(x=100, y = 70)
button_mult = Button(root, text="*", width= 5, height= 3,command=lambda:multiplicar()).place(x=160, y = 70)
button_div = Button(root, text="/", width= 5, height= 3,command=lambda:dividir()).place(x=220, y = 70)


def suma():
    try:
        input_text.set(var1.get()+var2.get())
    except:
        input_text.set("Error")


def resta():
    try:
        input_text.set(var1.get()-var2.get())
    except:
        input_text.set("Error")

def dividir():
    try:
        input_text.set(var1.get()/var2.get())
    except ZeroDivisionError:
        input_text.set("Math Error")
def multiplicar():
    try:
        input_text.set(var1.get()*var2.get())
    except:
        input_text.set("Error")

root.mainloop()