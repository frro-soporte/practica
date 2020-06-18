from tkinter import *
from tkinter import ttk
import tkinter as tk

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio


def show_alta():
    # Ventana alta
    a = Toplevel(ventana)
    a.title("Alta Socios")
    a.geometry("300x200")

    Label(a, text="Nombre").grid(column=0, row=1)
    nomb = StringVar()
    Entry(a, textvariable=nomb).grid(column=1, row=1)

    Label(a, text="Apellido").grid(column=0, row=2)
    ape = StringVar()
    Entry(a, textvariable=ape).grid(column=1, row=2)

    Label(a, text="DNI").grid(column=0, row=3)
    dni = StringVar()
    Entry(a, textvariable=dni).grid(column=1, row=3)

    Button(a, text="Aceptar", command=lambda: alta).grid(column=0, row=4)
    Button(a, text="Cancelar", command=lambda: quit).grid(column=1, row=4)

    def alta():
        negocio = NegocioSocio()
        if dni.get() != "" and nomb.get() != "" and ape.get() != "":
            socio = negocio.alta(Socio(dni=dni.get(), nombre=nomb.get(), apellido=ape.get()))
            if socio is not None:
                treeview.insert("", tk.END, text=socio.id_socio, values=(socio.nombre, socio.apellido, socio.dni))
            else:
                tk.messagebox.showerror("Error de usuario", "No pueden quedar campos vacios ")

    # Ventana modificar


def show_modificar():
    def modificar():  # falta esto
        negocio = NegocioSocio()
        sel = treeview.selection()[0]
        diccionario = treeview.item(sel)
        id_socio = diccionario['text']
        socio_mod = negocio.modificacion(Socio(dni=dni.get(), nombre=nomb.get(), apellido=ape.get()))
        if socio_mod:
            treeview.delete(sel)
            treeview.insert("", tk.END, text=socio_mod.id_socio,
                            values=(socio_mod.nombre, socio_mod.apellido, socio_mod.dni))
        else:
            tk.messagebox.showerror("Error de datos", "No cumple los requisitos ")

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

    Button(a, text="Aceptar", command=lambda: modificar, width=8, height=1).grid(column=0, row=4)
    Button(a, text="Cancelar", command=lambda: quit, width=8, height=1).grid(column=1, row=4)

    # Ventana baja


def show_baja():
        sel = treeview.selection()[0]
        idSocio = treeview.item(sel,option="text")
        socioNegocio = NegocioSocio.DatosSocio()
        socioNegocio.baja(idSocio)
        treeview.delete(sel)

# Ventana principal
ventana = Tk()
ventana.geometry("700x330")
ancho = 15
altura = 3

# Define arbol (tree)
treeview = ttk.Treeview(ventana)

treeview["columns"] = ("one", "two", "three")
treeview.column("#0", width=100)
treeview.column("one", width=200)
treeview.column("two", width=200)
treeview.column("three", width=200)

treeview.heading("#0", text="Id")
treeview.heading("one", text="Nombre")
treeview.heading("two", text="Apellido")
treeview.heading("three", text="DNI")

# Define botones
boton1 = Button(ventana, text="Alta", command=show_alta(), width=ancho, height=altura).grid(column=0, row=2)
boton2 = Button(ventana, text="Baja", command=show_baja, width=ancho, height=altura).grid(column=1, row=2)
boton3 = Button(ventana, text="Modificación ", command=show_modificar(), width=ancho, height=altura).grid(column=2,
                                                                                                          row=2)


def carga_socios():
    datos = NegocioSocio()
    socios = datos.todos()
    for socio in socios:
        treeview.insert("", tk.END, text=socio.id, values=(socio.nombre, socio.apellido, socio.dni))
    treeview.pack


ventana.title("Socios")
carga_socios()
ventana.mainloop()
