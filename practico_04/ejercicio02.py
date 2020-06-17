## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 
from tkinter import *
from tkinter import ttk, font

def ver(a):
    valor.set(valor.get() + a)

def igual():
    valor.set(eval(valor.get()))

window = Tk()
window.title('Calculadora')
marco = ttk.Frame(window, borderwidth=2, relief="raised", padding=(10,10))
marco.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = (N, S, E, W))
valor = StringVar()

visor = Entry(marco, width=50, textvariable = valor)

uno = Button(marco, text="1", command = lambda: ver('1'))
dos = Button(marco, text="2", command= lambda: ver('2'))
tres = Button(marco, text="3", command= lambda: ver('3'))
cuatro = Button(marco, text="4", command= lambda: ver('4'))
cinco = Button(marco, text="5", command= lambda: ver('5'))
seis = Button(marco, text="6", command= lambda: ver('6'))
siete = Button(marco, text="7", command= lambda: ver('7'))
ocho = Button(marco, text="8", command= lambda: ver('8'))
nueve = Button(marco, text="9", command= lambda: ver('9'))
cero = Button(marco, text="0", command= lambda: ver('0'))

mas = Button(marco, text = '+', command = lambda: ver('+'))
menos = Button(marco, text = '-', command = lambda: ver('-'))
mult = Button(marco, text = '*', command = lambda: ver('*'))
divis = Button(marco, text = '/', command = lambda: ver('/'))
igual = Button(marco, text = '=', command = igual)

visor.grid(column=1, row=0,padx = 5, pady = 5, sticky = ( E, W), columnspan = 4)
uno.grid(column=1, row=9,padx = 5, pady = 5, sticky = ( E, W))
dos.grid(column=2, row=9,padx = 5, pady = 5, sticky = ( E, W))
tres.grid(column=3, row=9,padx = 5, pady = 5, sticky = ( E, W))
cuatro.grid(column=1, row=6,padx = 5, pady = 5, sticky = ( E, W))
cinco.grid(column=2, row=6,padx = 5, pady = 5, sticky = ( E, W))
seis.grid(column=3, row=6,padx = 5, pady = 5, sticky = ( E, W))
siete.grid(column=1, row=3,padx = 5, pady = 5, sticky = ( E, W))
ocho.grid(column=2, row=3,padx = 5, pady = 5, sticky = ( E, W))
nueve.grid(column=3, row=3,padx = 5, pady = 5, sticky = ( E, W))
cero.grid(column=2, row=12,padx = 5, pady = 5, sticky = ( E, W))

mas.grid(column=4, row=3,padx = 5, pady = 5, sticky = ( E, W))
menos.grid(column=4, row=6,padx = 5, pady = 5, sticky = ( E, W))
mult.grid(column=4, row=9,padx = 5, pady = 5, sticky = ( E, W))
divis.grid(column=4, row=12,padx = 5, pady = 5, sticky = ( E, W))
igual.grid(column=4, row=15,padx = 5, pady = 5, sticky = ( E, W))


window.mainloop()