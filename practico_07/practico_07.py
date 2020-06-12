"""
Tp7 – Capa Presentacion Socios
Crear en Python usando Tkinter un formulario para gestionar los datos de Socios usando la Clase de la Capa de Negocio Socios .
El Formulario principal tiene que mostrar todos los socios en Treeview y tener los siguientes botones Alta , Baja , Modificar .
Apretar el Boton Alta se tiene que abrir un formulario con los campos para ingresar los datos de socio .
Incluye  2 botones Guardar y Cancelar.
Apretar el Boton Baja se tiene que dar de baja el socio seleccionado .
Apretar el Boton Modificar se tiene que abrir un formulario con los campos con los datos del socio seleccionado .
Incluye 2 botones Aceptar y Cancelar .
"""

from tkinter import *
from practico_06 import capa_negocio
from tkinter import ttk, messagebox
import tkinter as tk
from practico_05.ejercicio_01 import Socio
import easygui as eg
#import easygui as eg


def alta():
    e = Toplevel(root)
    e.title("Ingresar nuevo Socio")
    e.geometry('250x120')
    Label(e, text="Ingrese el Dni").grid(column=0, row=0)
    dni = IntVar()
    Entry(e, textvariable=dni).grid(column=1, row=0)

    Label(e, text="Ingrese el nombre").grid(column=0, row=1)
    nombre = StringVar()
    Entry(e, textvariable=nombre).grid(column=1, row=1)

    Label(e, text="Ingrese el apellido").grid(column=0, row=2)
    apellido = StringVar()
    Entry(e, textvariable=apellido).grid(column=1, row=2)

    Button(e, text="Cancelar", command=lambda: cancelar()).grid(column=1, row=4)
    def cancelar():
        e.destroy()

    Button(e, text="Guardar", command=lambda: guardar(dni,nombre,apellido)).grid(column=0, row=4)

    def guardar(dni,nombre,apellido):
        if (dni.get()>0 and len(nombre.get())>0 and len(apellido.get())>0):
            socio = Socio(dni=dni.get(), nombre=nombre.get(), apellido=apellido.get())
            socioNegocio = capa_negocio.DatosSocio()
            socioNegocio.alta(socio)
            socio = socioNegocio.buscar_dni(dni.get())
            tree.insert("", tk.END, text=socio.id, values=(socio.dni, socio.nombre, socio.apellido))
            e.destroy()
        else:
            messagebox.showinfo(message="Datos Invalidos", title="Error")
            #eg.msgbox(msg="Completa los datos para continuar",title="Datos faltantes", ok_button="continuar")

def baja():
    try:
        item = tree.selection()[0]
        idSocio = tree.item(item,option="text")
        socioNegocio = capa_negocio.DatosSocio()
        socioNegocio.baja(idSocio)
        tree.delete(item)
    except:
        messagebox.showinfo(message="Selecciona un socio para continuar", title="Error")

def modificacion():
    try:
        item = tree.selection()[0]
        idSocio = tree.item(item, option="text")
        socioNegocio = capa_negocio.DatosSocio()
        socio = socioNegocio.buscar(idSocio)

        e = Toplevel(root)
        e.title("Ingresar nuevo Socio")
        e.geometry('250x120')
        Label(e, text="Ingrese el Dni").grid(column=0, row=0)
        dni = IntVar()
        dni.set(socio.dni)
        Entry(e, textvariable=dni).grid(column=1, row=0)

        Label(e, text="Ingrese el nombre").grid(column=0, row=1)
        nombre = StringVar()
        nombre.set(socio.nombre)
        Entry(e, textvariable=nombre).grid(column=1, row=1)

        Label(e, text="Ingrese el apellido").grid(column=0, row=2)
        apellido = StringVar()
        apellido.set(socio.apellido)
        Entry(e, textvariable=apellido).grid(column=1, row=2)
        
        Button(e, text="Cancelar", command=lambda: cancelar()).grid(column=1, row=4)
        def cancelar():
            e.destroy()

        Button(e, text="Guardar", command=lambda: guardar(dni, nombre, apellido)).grid(column=0, row=4)

        def guardar(dni,nombre,apellido):
            if (dni.get() > 0 and len(nombre.get()) > 0 and len(apellido.get()) > 0):
                socio.dni = dni.get()
                socio.nombre = nombre.get()
                socio.apellido = apellido.get()
                socioNegocio.modificacion(socio)
                tree.item(item,text=socio.id, values=(socio.dni,socio.nombre,socio.apellido))
                e.destroy()
            else:
                messagebox.showinfo(message="Completa los datos para continuar", title="Error")

    except IndexError:
        messagebox.showinfo(message="Selecciona un socio para continuar", title="Error")
        #eg.msgbox(msg="Selecciona un socio para continuar", title="Datos faltantes", ok_button="continuar")
    except:
        messagebox.showinfo(message="Completa los datos para continuar", title="Error")
        #eg.msgbox(msg="Completa los datos para continuar", title="Datos faltantes", ok_button="continuar")


def cargarTabla(tree):
    tree["columns"] = ("dni", "nombre", "apellido")
    tree.column('#0',width=100)
    tree.column('dni',width=150)
    tree.column('nombre',width=150)
    tree.column('apellido',width=150)
    tree.heading('#0', text='ID')
    tree.heading('dni',text='DNI')
    tree.heading('nombre',text='Nombre')
    tree.heading('apellido',text='apellido')

    negocioSocio = capa_negocio.NegocioSocio()
    totalSocios = negocioSocio.todos()

    for i in totalSocios:
        tree.insert("", tk.END, text=i.id, values=(i.dni, i.apellido, i.nombre))
    tree.pack()

root = Tk()
root.resizable(False,False)
root.geometry('600x200')
root.configure(bg = 'beige')
root.title('-- ABM SOCIOS --')
ttk.Button(root, text='Salir',command=root.destroy).pack(side=BOTTOM)
tree = ttk.Treeview()
cargarTabla(tree)

ttk.Button(root,text='alta',command=alta).place(x=20,y=175)
ttk.Button(root,text='modificar',command=modificacion).place(x=100,y=175)
ttk.Button(root,text='eliminar',command=baja).place(x=180,y=175)

root.mainloop()
#s
