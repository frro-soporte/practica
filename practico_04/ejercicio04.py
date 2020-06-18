## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 

from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.title("Ciudades")
ancho=15
altura=3

def alta():
    a = Toplevel(ventana)
    a.title("Alta")
    Label(a, text="Ingrese la ciudad").grid(column=0, row=0)
    ciudad = StringVar()
    Entry(a, textvariable=ciudad).grid(column=1, row=0)
    Label(a, text="Ingrese el CP").grid(column=0, row=2)
    codigo = StringVar()
    Entry(a, textvariable=codigo).grid(column=1, row=2)
    Button(a, text="Cargar", command= lambda : guardar(ciudad,codigo),width=8,height=1).grid(column=0, row=3,columnspan=2)

    def guardar(ciudad, codigo):
        treeview.insert("", END, text=(ciudad.get() + " " + codigo.get()))
        a.destroy()

def baja():
    sel = treeview.selection()[0]
    treeview.delete(sel)

def modi():
    sel = treeview.selection()[0]
    ciudadCodigo = treeview.item(sel)["text"]
    m = Toplevel(ventana)
    m.title("Modificación")
    Label(m, text="Ingrese la ciudad").grid(column=0, row=0)
    ciudad = StringVar()
    ciudad.set(ciudadCodigo[:ciudadCodigo.find(" ")])
    Entry(m, textvariable=ciudad).grid(column=1, row=0)
    Label(m, text="Ingrese el CP").grid(column=0, row=2)
    codigo = StringVar()
    codigo.set(ciudadCodigo[ciudadCodigo.find(" "):])
    Entry(m, textvariable=codigo).grid(column=1, row=2)
    Button(m, text="Guardar", command= lambda : guardar(ciudad,codigo),width=8,height=1).grid(column=0, row=3,columnspan=2)

    def guardar(ciudad, codigo):
        treeview.item(sel, text=(ciudad.get() + " " + codigo.get()))
        m.destroy()



treeview = ttk.Treeview(ventana)
treeview.insert("",END, text = "Rosario 2000")
treeview.insert("",END, text = "Santa fe 3000")
treeview.insert("",END, text = "Mendoza 5500")
treeview.insert("",END, text = "Cordoba 5000")
treeview.insert("",END, text = "Corrientes 3400")
treeview.grid(column = 0, row = 0,columnspan=3)
z= Label(ventana,text="ABM Ciudades").grid(column = 1,row=1)
boton1= Button(ventana,text="Alta", command=alta,width=ancho,height=altura).grid(column = 0,row=2)
boton2= Button(ventana,text="Baja", command=baja,width=ancho,height=altura).grid(column = 1,row=2)
boton4= Button(ventana,text="Modificación ", command=modi,width=ancho,height=altura).grid(column = 2,row=2)

ventana.mainloop()

