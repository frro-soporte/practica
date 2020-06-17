
from tkinter import *
from tkinter import ttk
import tkinter
from practico_06.capa_negocio import NegocioSocio

def alta():#hay q cambiar lo de adentro
    def alt():#falta esto
        pass

    a = Toplevel(ventana)
    a.title("Alta")
    Label(a, text="ID").grid(column=0, row=0)
    id = IntVar()
    Entry(a, textvariable=id).grid(column=1, row=0)

    Label(a, text="Nombre").grid(column=0, row=1)
    nomb = StringVar()
    Entry(a, textvariable=nomb).grid(column=1, row=1)

    Label(a, text="Apellido").grid(column=0, row=2)
    ape = StringVar()
    Entry(a, textvariable=ape).grid(column=1, row=2)

    Label(a, text="DNI").grid(column=0, row=3)
    dni = StringVar()
    Entry(a, textvariable=dni).grid(column=1, row=3)

    tkinter.Button(a, text="Aceptar", command = alt,width=8,height=1).grid(column=0, row=4)
    tkinter.Button(a, text="Cancelar", command = quit,width=8,height=1).grid(column=1, row=4)


def modi():
    def modificar():#falta esto
        pass

    a = Toplevel(ventana)
    a.title("Modificar")
    Label(a, text="ID").grid(column=0, row=0)
    id = IntVar()
    Entry(a, textvariable=id).grid(column=1, row=0)

    Label(a, text="Nombre").grid(column=0, row=1)
    nomb = StringVar()
    Entry(a, textvariable=nomb).grid(column=1, row=1)

    Label(a, text="Apellido").grid(column=0, row=2)
    ape = StringVar()
    Entry(a, textvariable=ape).grid(column=1, row=2)

    Label(a, text="DNI").grid(column=0, row=3)
    dni = StringVar()
    Entry(a, textvariable=dni).grid(column=1, row=3)

    tkinter.Button(a, text="Aceptar", command = modificar,width=8,height=1).grid(column=0, row=4)
    tkinter.Button(a, text="Cancelar", command = quit,width=8,height=1).grid(column=1, row=4)



def baja():
    def borrar():#falta esto
        pass

    baja = tkinter.Toplevel(ventana)
    baja.title ("Baja")
    #Labels y Botones
    tkinter.Label(baja, text="¿Está seguro que desea eliminar a este Socio?").grid(column=0, row=0,columnspan=2)
    tkinter.Button(baja, text="Eliminar", command = borrar,width=8,height=1).grid(column=0, row=1)
    tkinter.Button(baja, text="Cancelar", command = quit,width=8,height=1).grid(column=1, row=1)




ventana=Tk()
ventana.title("Socios")
ancho=15
altura=3

treeview = ttk.Treeview(ventana)

treeview["columns"]=("one", "two", "three")
treeview.column("#0", width=100, minwidth=100)
treeview.column("#1", width=200, minwidth=200)
treeview.column("#2", width=200, minwidth=200)
treeview.column("#3", width=200, minwidth=200)

treeview.heading("#0",text="Id",anchor=tkinter.W)
treeview.heading("#1", text="Nombre",anchor=tkinter.W)
treeview.heading("#2", text="Apellido",anchor=tkinter.W)
treeview.heading("#3", text="DNI",anchor=tkinter.W)

treeview.insert("",END, text = "Rosario 2000")
treeview.insert("",END, text = "Santa fe 3000")
treeview.insert("",END, text = "Mendoza 5500")
treeview.insert("",END, text = "Cordoba 5000")
treeview.insert("",END, text = "Corrientes 3400")
treeview.grid(column = 0, row = 0,columnspan=3)

boton1= Button(ventana,text="Alta", command=alta,width=ancho,height=altura).grid(column = 0,row=2)
boton2= Button(ventana,text="Baja", command=baja,width=ancho,height=altura).grid(column = 1,row=2)
boton4= Button(ventana,text="Modificación ", command=modi,width=ancho,height=altura).grid(column = 2,row=2)

ventana.mainloop()
