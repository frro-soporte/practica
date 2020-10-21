import sys
sys.path.append('c:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23 - Copy/practico_06')
sys.path.append('c:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23 - Copy/practico_05')

from capa_negocio import DniRepetido
from capa_negocio import LongitudInvalida
from capa_negocio import MaximoAlcanzado
from capa_negocio import NegocioSocio
from ejercicio_01 import Socio
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

class PresentacionSocio:

    def __init__(self, SociosDesktop):
        self.SociosDesktop = SociosDesktop
        self.SociosDesktop.title("Socios")

        self.negocio = NegocioSocio()
        

    def Socios(self):  

        frameBtn = tk.Frame(self.SociosDesktop)
        frameBtn.grid(row=0, column=0, columnspan=3, pady=20) 

        btnAgregar = tk.Button(frameBtn, text="Agregar", command=self.newSocio)
        btnAgregar.pack(side = LEFT, expand = True)

        btnDelete = tk.Button(frameBtn, text="Eliminar", command=self.deleteSocio)
        btnDelete.pack(side = LEFT, expand = True)

        btnModificar = tk.Button(frameBtn, text="Modificar", command=self.modifySocio)
        btnModificar.pack(side = LEFT, expand = True)
        
        frameBtn.pack(side = TOP) 

        self.trv= ttk.Treeview(self.SociosDesktop)
        self.trv = ttk.Treeview(self.SociosDesktop, columns=("surname", "name", "dni"))
        self.trv.heading("#0", text="ID")
        self.trv.heading("surname", text="Apellido")
        self.trv.heading("name", text="Nombre")
        self.trv.heading("dni", text="DNI")

        self.listarSocios()

    def listarSocios(self):  
        self.trv.delete(*self.trv.get_children())        
        listaSocios = self.negocio.todos()
        for socio in listaSocios:
             self.trv.insert("", tk.END, text=socio.id,
                             values=(socio.apellido, socio.nombre, socio.dni))
        self.trv.pack(side = BOTTOM )
    

    def newSocio(self):
        self.new = tk.Toplevel(self.SociosDesktop)
        self.new.grab_set()

        frame = LabelFrame(self.new, text="Ingresar Nuevo Socio")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        lblsurname = ttk.Label(frame, text="Apellido: ")
        lblsurname.grid(column=0, row=1)

        self.strvSurname = tk.StringVar()
        txtSurname = ttk.Entry(frame, width=15, textvariable=self.strvSurname)
        txtSurname.focus()
        txtSurname.grid(column=1, row=1)

        lblPC = ttk.Label(frame, text="Nombre: ")
        lblPC.grid(column=0, row=2)

        self.strvName = tk.StringVar()
        txtName = ttk.Entry(frame, width=15, textvariable=self.strvName)
        txtName.grid(column=1, row=2)

        lbldni = ttk.Label(frame, text="DNI: ")
        lbldni.grid(column=0, row=3)

        self.strvDni = tk.StringVar()
        txtDni = ttk.Entry(frame, width=15, textvariable=self.strvDni)
        txtDni.grid(column=1, row=3)
        
        btnSave = ttk.Button(frame, text="Guardar Socio", command=self.addSocio)
        btnSave.grid(column=2, row=5, columnspan=2)

        btnCancelar = ttk.Button(frame, text="Cancelar", command=self.new.destroy)
        btnCancelar.grid(column=0, row=5, columnspan=2)
        

    def addSocio(self):
        self.socioActual = Socio()
        try:
            self.socioActual.apellido = self.strvSurname.get()
            self.socioActual.nombre = self.strvName.get()
            self.socioActual.dni = int(self.strvDni.get())
            self.negocio.alta(self.socioActual)
            self.listarSocios()
            self.new.destroy()
        except ValueError :
            messagebox.showinfo("Imposible Crear Usuario", "El DNI solo debe contener digitos numericos")
        except DniRepetido as dr:
            messagebox.showinfo("Imposible Crear Usuario", dr.args[0])
        except LongitudInvalida as li:
            messagebox.showinfo("Imposible Crear Usuario", li.args[0])
        except MaximoAlcanzado as ma:
            messagebox.showinfo("Imposible Crear Usuario", ma.args[0])

    def deleteSocio(self):
        curItem = self.trv.item(self.trv.selection())
        id = int(curItem["text"]) 
        self.negocio.baja(id)
        self.listarSocios()
       

    def modifySocio(self):
        self.socioActual = Socio()
        try:
            curItem = self.trv.item(self.trv.selection())
            id = int(curItem["text"])
            self.socioActual = self.negocio.buscar(id)

            self.new = tk.Toplevel(self.SociosDesktop)
            self.new.grab_set()

            frame = LabelFrame(self.new, text="Modificar Socio")
            frame.grid(row=0, column=0, columnspan=3, pady=20)

            lblsurname = ttk.Label(frame, text="Apellido: ")
            lblsurname.grid(column=0, row=1)

            self.strvSurname = tk.StringVar()
            txtSurname = ttk.Entry(frame, width=15, textvariable=self.strvSurname)
            txtSurname.insert(0,self.socioActual.apellido)
            txtSurname.focus()
            txtSurname.grid(column=1, row=1)

            lblPC = ttk.Label(frame, text="Nombre: ")
            lblPC.grid(column=0, row=2)

            self.strvName = tk.StringVar()
            txtName = ttk.Entry(frame, width=15, textvariable=self.strvName)
            txtName.insert(0,self.socioActual.nombre)
            txtName.grid(column=1, row=2)

            lbldni = ttk.Label(frame, text="DNI: ")
            lbldni.grid(column=0, row=3)

            self.strvDni = tk.StringVar()
            txtDni = ttk.Entry(frame, width=15, textvariable=self.strvDni)
            txtDni.insert(0,self.socioActual.dni)
            txtDni.grid(column=1, row=3)
            
            btnSave = ttk.Button(frame, text="Guardar Socio", command=self.updateSocio)
            btnSave.grid(column=2, row=5, columnspan=2)

            btnCancelar = ttk.Button(frame, text="Cancelar", command=self.new.destroy)
            btnCancelar.grid(column=0, row=5, columnspan=2)
        except ValueError:
            messagebox.showinfo("Atencion", "No ha seleccionado ningun usuario a modificar") 


    def updateSocio(self):
        try:
            self.socioActual.apellido = self.strvSurname.get()
            self.socioActual.nombre = self.strvName.get()
            self.socioActual.dni = int(self.strvDni.get())
            self.negocio.modificacion(self.socioActual)
            self.listarSocios()
            self.new.destroy()
        except ValueError :
            messagebox.showinfo("Imposible Crear Usuario", "El DNI solo debe contener digitos numericos")
        except LongitudInvalida as li:
            messagebox.showinfo("Imposible Actualizar Usuario", li.args[0])
  
        

if __name__ == '__main__':
    SociosWindow = Tk()
    application = PresentacionSocio(SociosWindow)
    application.Socios()
    SociosWindow.mainloop()