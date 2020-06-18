## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 

from tkinter import  *
from tkinter import ttk
import tkinter as tk

def acept(a,b, v2):
    x = arbol.insert("", tk.END, text = a)
    arbol.insert(x, "end", text = b)
    v2.destroy()


def falta():
    v2 = Tk()
    v2.title('Alta ciudad')
    cid = Label(v2, width = 50, text = 'Ingrese ciudad:')
    icp = Label(v2, width = 50, text = 'Ingrese codigo postal:')
    city = Entry(v2,  width=50)
    cod = Entry(v2,  width=50)
    cid.grid()
    city.grid()
    icp.grid()
    cod.grid()
    ok = Button(v2, text = 'Ok', command = lambda: acept(city.get(), cod.get(), v2))
    ok.grid()
    v2.mainloop()

def fmodif(arbol):
    v2 = Tk()
    v2.title('Modificacion ciudad')
    et = Label(v2, width = 50, text = 'Coidigo Postal:')
    cod = Entry(v2, width=50)
    et.grid()
    cod.grid()
    ok = Button(v2, text='Ok', command=lambda: am(v2, arbol, cod))
    ok.grid()
    v2.mainloop()

def am(v2, arbol, cod):
    i = arbol.focus()
    m = arbol.get_children(i)
    arbol.item(m[0], text=cod.get())
    v2.destroy()

def fbaja(arbol):
    i=arbol.focus()
    arbol.delete(i)

window = Tk()
window.title('Ciudades Argentinas')
arbol = ttk.Treeview()

arbol["columns"]=("one")

arbol.heading("#0",text="Ciudad")

# Level 1
rosario = arbol.insert("", tk.END, text="Rosario")
cordoba = arbol.insert("", tk.END, text="Cordoba")
salta = arbol.insert("", tk.END, text="Salta")
resistencia = arbol.insert("", tk.END, text="Resistencia")
sn = arbol.insert("", tk.END, text="San Nicolas")

# Level 2
arbol.insert(rosario, "end", text="2000")
arbol.insert(cordoba, "end", text="5000")
arbol.insert(salta, "end", text="4400")
arbol.insert(resistencia, "end", text="3500")
arbol.insert(sn, "end", text="2900")

alta = Button(window, text = 'Alta', command = falta)
modif = Button(window, text = 'Modificacion', command = lambda: fmodif(arbol))
baja = Button(window, text = 'Baja', command = lambda: fbaja(arbol))

arbol.grid()
alta.grid()
modif.grid()
baja.grid()

window.mainloop()