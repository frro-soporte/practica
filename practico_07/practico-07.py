from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio
from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self):
        self.app = Tk()
        self.app.title("Socios")
        self.frame = Frame(self.app)
        self.frame.grid(column=0, row=0)
        self.treeview = ttk.Treeview(self.frame, columns=("one", "two", "three"))
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("one", text="Nombre")
        self.treeview.heading("two", text="Apellido")
        self.treeview.heading("three", text="DNI")
        self.treeview.pack()
        self.ns = NegocioSocio()
        self.menu = Frame(self.app)
        self.menu.grid(row=1, column=0)
        self.datos = Frame(self.app)
        self.datos.grid(row=2, column=0)
        self.muestraDatos()
        ttk.Button(self.menu, text="Alta", command=self.alta).grid(row=0, column=0)
        ttk.Button(self.menu, text="Modificacion", command=self.modificacion).grid(row=0, column=1)
        ttk.Button(self.menu, text="Baja", command=self.baja).grid(row=0, column=2)

        self.app.mainloop()

    def muestraDatos(self):
        self.limpiarGrilla()
        socios = self.ns.todos()
        for socio in socios:
            self.cargarDatos(socio)

    def cargarDatos(self, socio):
        self.treeview.insert("", END, text=socio.id, values=(socio.nombre, socio.apellido, socio.dni))

    def alta(self):
        self.limpiarGrilla()
        ttk.Label(self.datos, text="Apellido:").grid(column=0, row=1)
        ttk.Label(self.datos, text="Nombre:").grid(column=0, row=2)
        ttk.Label(self.datos, text="DNI:").grid(column=0, row=3)
        self.apellido = ttk.Entry(self.datos, text="")
        self.apellido.grid(column=1, row=1, columnspan=2)
        self.nombre = ttk.Entry(self.datos, text="")
        self.nombre.grid(column=1, row=2, columnspan=2)
        self.dni = ttk.Entry(self.datos, text="")
        self.dni.grid(column=1, row=3, columnspan=2)
        self.errorCampo = ttk.Label(self.datos, text="")
        self.errorCampo.grid(column=0, row=5)
        ttk.Button(self.datos, text="Confirmar", command=lambda: self.agregar()).grid(row=4, column=0)
        ttk.Button(self.datos, text="Cancelar", command=lambda: self.limpiarGrilla()).grid(row=4, column=1)

    def agregar(self):
        self.errorCampo.grid_remove()
        self.errorCampo = ttk.Label(self.datos, text="")
        self.errorCampo.grid(column=0, row=5)
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        dni = self.dni.get()
        if nombre == "" or apellido == "" or dni == "":
            self.errorCampo.config(text="Debe completar todos los campos")
        else:
            socio = Socio(dni=dni, apellido=apellido, nombre=nombre)
            try:
                self.ns.alta(socio)
                self.cargarDatos(socio)
            except Exception as e:
                self.errorCampo.config(text=e)


    def modificacion(self):
        self.limpiarGrilla()
        try:
            idPersona = self.treeview.focus()
            if self.treeview.item(idPersona)['text'] == "":
                ttk.Label(self.datos, text="Debe seleccionar una fila a modificar").grid(column=0, row=1)
            else:
                ttk.Label(self.datos, text="Nombre:").grid(column=0, row=1)
                ttk.Label(self.datos, text="Apellido:").grid(column=0, row=2)
                ttk.Label(self.datos, text="DNI:").grid(column=0, row=3)
                self.idSocio = self.treeview.item(idPersona)['text']
                self.nombre = ttk.Entry(self.datos, text="")
                self.nombre.grid(column=1, row=1, columnspan=2)
                self.nombre.insert(END, self.treeview.item(idPersona)['values'][0])
                self.apellido = ttk.Entry(self.datos, text="")
                self.apellido.grid(column=1, row=2, columnspan=2)
                self.apellido.insert(END, self.treeview.item(idPersona)['values'][1])
                self.dni = ttk.Entry(self.datos, text="")
                self.dni.grid(column=1, row=3, columnspan=2)
                self.dni.insert(END, self.treeview.item(idPersona)['values'][2])
                self.errorCampo = ttk.Label(self.datos, text="")
                self.errorCampo.grid(column=0, row=5)
                ttk.Button(self.datos, text="Confirmar", command=lambda: self.modificar(idPersona)).grid(row=4, column=0)
                ttk.Button(self.datos, text="Cancelar", command=lambda: self.limpiarGrilla()).grid(row=4, column=1)
        except:
            ttk.Label(self.datos, text="Debe seleccionar una fila a modificar").grid(column=0, row=5)

    def modificar(self, idPersona):
        try:
            self.errorCampo.grid_remove()
            self.errorCampo = ttk.Label(self.datos, text="")
            self.errorCampo.grid(column=0, row=5)
            idSocio = self.idSocio
            nombre = self.nombre.get()
            apellido = self.apellido.get()
            dni = self.dni.get()
            if nombre == "" or apellido == "" or dni == "":
                self.errorCampo.config(text="Debe completar todos los campos")
            else:
                try:
                    socio = Socio(id=idSocio, dni=dni, apellido=apellido, nombre=nombre)
                    if self.ns.modificacion(socio):
                        self.treeview.insert("", self.treeview.index(idPersona)+1, text=idSocio, values=(nombre, apellido, dni))
                        self.treeview.delete(idPersona)
                        self.limpiarGrilla()
                        ttk.Label(self.datos, text="Modificado").grid(column=0, row=5)
                    else:
                        ttk.Label(self.datos, text="No se pudo modificar").grid(column=0, row=5)
                except Exception as e:
                    self.errorCampo.config(text=e)
        except:
            ttk.Label(self.datos, text="Debe seleccionar una fila a modificar").grid(column=0, row=5)

    def baja(self):
        self.limpiarGrilla()
        try:
            idPersona = self.treeview.focus()
            try:
                idSocio = self.treeview.item(idPersona)['text']
                if self.ns.baja(id_socio=idSocio):
                    self.treeview.delete(idPersona)
                    self.limpiarGrilla()
                    ttk.Label(self.datos, text="Baja confirmada").grid(column=0, row=1)
                else:
                    ttk.Label(self.datos, text="No se pudo eliminar").grid(column=0, row=1)
            except Exception as e:
                self.errorCampo.config(text=e)
        except:
            ttk.Label(self.datos, text="Debe seleccionar una fila a borrar").grid(column=0, row=1)

    def limpiarGrilla(self):
        self.datos.grid_remove()
        self.datos = Frame(self.app)
        self.datos.grid(row=2, column=0)


app = Application()


