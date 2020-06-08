import sys
sys.path.append('c:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_06')

import tkinter as tk
from tkinter import ttk
from tkinter import *

class Socio:

    def __init__(self, SociosDesktop):
        self.SociosDesktop = SociosDesktop
        self.SociosDesktop.title("Socios")

    def Socios(self):
        btnsurname = tk.Button(SociosWindow, text="Agregar", command=self.newSocio)
        btnsurname.grid(row=0)
        btnsurname.pack()

        btnDelete = tk.Button(SociosWindow, text="Eliminar", command=self.deleteSocio)
        btnDelete.pack()

        btnModificar = tk.Button(SociosWindow, text="Modificar", command=self.modifySocio)
        btnModificar.pack()

        self.trv = ttk.Treeview(SociosWindow)
        self.trv.pack()

    def newSocio(self):
        new = tk.Toplevel(SociosWindow)

        frame = LabelFrame(new, text="Ingresar Nuevo Socio")
        frame.grid(row=0, column=0, columnspan=2, pady=20)

        lblsurname = ttk.Label(frame, text="Apellido: ")
        lblsurname.grid(column=0, row=1)

        self.surname = tk.StringVar()
        self.txtSurname = ttk.Entry(frame, width=15, textvariable=self.surname)
        self.txtSurname.focus()
        self.txtSurname.grid(column=1, row=1)

        lblPC = ttk.Label(frame, text="Nombre: ")
        lblPC.grid(column=0, row=2)

        self.name = tk.StringVar()
        self.txtName = ttk.Entry(frame, width=15, textvariable=self.name)
        self.txtName.grid(column=1, row=2)

        lbldni = ttk.Label(frame, text="DNI: ")
        lbldni.grid(column=0, row=3)

        self.dni = tk.StringVar()
        self.txtDni = ttk.Entry(frame, width=15, textvariable=self.dni)
        self.txtDni.grid(column=1, row=3)

        btnSave = ttk.Button(frame, text="Guardar Socio", command=self.addSocio)
        btnSave.grid(column=1, row=4, columnspan=2)

    def addSocio(self):
        self.trv.insert("", "end", text=self.Socio.get(), values=(self.pc.get()))
        #self.txtSocio.delete(0, END)
        #self.txtPC.delete(0, END)

    def deleteSocio(self):
        item = self.trv.selection()
        self.trv.delete(item)

    def modifySocio(self):
        try:
            self.trv.item(self.trv.selection())['text'][0]
        except IndexError as e:
            # mostrar error
            return

        new = tk.Toplevel(SociosWindow)

        frame = LabelFrame(new, text="Modifica una Socio")
        frame.grid(row=0, column=0, columnspan=2, pady=20)

        curItem = self.trv.item(self.trv.selection())

        lblName = ttk.Label(frame, text="Nombre viejo")
        lblName.grid(column=0, row=1)

        lblName = ttk.Label(frame, text=curItem["text"])
        lblName.grid(column=1, row=1)

        lblName = ttk.Label(frame, text="Nombre nuevo: ")
        lblName.grid(column=0, row=2)

        self.name = tk.StringVar()
        self.txtName = ttk.Entry(frame, width=15, textvariable=self.name)
        self.txtName.focus()
        self.txtName.grid(column=1, row=2)

        lblsurname = ttk.Label(frame, text="Apellido viejo")
        lblsurname.grid(column=0, row=1)

        lblsurname = ttk.Label(frame, text=curItem["text"])
        lblsurname.grid(column=1, row=1)

        lblsurname = ttk.Label(frame, text="Apellido nuevo: ")
        lblsurname.grid(column=0, row=2)

        self.surname = tk.StringVar()
        self.txtSurname = ttk.Entry(frame, width=15, textvariable=self.surname)
        self.txtSurname.focus()
        self.txtSurname.grid(column=1, row=2)

        btnSave = ttk.Button(frame, text="Guardar Socio", command=self.updateSocio)
        btnSave.grid(column=1, row=5, columnspan=2)

    def updateSocio(self):
        self.trv.item(self.trv.selection(), text=self.Socio.get(), values=(self.pc.get()))
        self.txtSocio.delete(0, END)
        self.txtPC.delete(0, END)


if __name__ == '__main__':
    SociosWindow = Tk()
    application = Socio(SociosWindow)
    application.Socios()
    SociosWindow.mainloop()