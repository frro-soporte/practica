## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 
from tkinter import *
from tkinter import ttk


class Application:
    def __init__(self):
        self.app = Tk()
        self.app.title("Ciudades argentinas")
        self.frame = Frame(self.app)
        self.frame.grid(column=0, row=0)
        self.treeview = ttk.Treeview(self.frame, columns="one")
        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("one", text="Codigo postal")
        self.treeview.pack()
        self.agregarciudad("rosario", "2000")
        self.agregarciudad("quilmes", "1879")
        self.agregarciudad("cordoba", "5000")
        self.agregarciudad("san rafael", "4000")
        self.agregarciudad("pehuajo", "5500")
        self.menu = Frame(self.app)
        self.menu.grid(row=1, column=0)
        self.datos = Frame(self.app)
        self.datos.grid(row=2, column=0)
        ttk.Button(self.menu, text="Alta", command=self.alta).grid(row=0, column=0)
        ttk.Button(self.menu, text="Modificacion", command=self.modificacion).grid(row=0, column=1)
        ttk.Button(self.menu, text="Baja", command=self.baja).grid(row=0, column=2)

        self.app.mainloop()

    def agregarciudad(self, nombre, codigo_postal):
        self.treeview.insert("", END, text=nombre, values=codigo_postal)

    def alta(self):
        self.limpiarGrilla()
        ttk.Label(self.datos, text="Ciudad:").grid(column=0, row=1)
        ttk.Label(self.datos, text="Codigo Postal:").grid(column=0, row=2)
        self.ciudad = ttk.Entry(self.datos, text="")
        self.ciudad.grid(column=1, row=1, columnspan=2)
        self.codigoPostal = ttk.Entry(self.datos, text="")
        self.codigoPostal.grid(column=1, row=2, columnspan=2)
        self.errorCampo = ttk.Label(self.datos, text="")
        self.errorCampo.grid(column=0, row=4)
        ttk.Button(self.datos, text="Confirmar", command=lambda: self.agregar()).grid(row=3, column=0)

    def agregar(self):
        self.errorCampo.grid_remove()
        self.errorCampo = ttk.Label(self.datos, text="")
        self.errorCampo.grid(column=0, row=4)
        ciudad = self.ciudad.get()
        cp = self.codigoPostal.get()
        if ciudad == "" or cp == "":
            self.errorCampo.config(text="Debe completar todos los campos")
        else:
            self.agregarciudad(ciudad, cp)

    def modificacion(self):
        self.limpiarGrilla()
        try:
            idCiudad = self.treeview.focus()
            if self.treeview.item(idCiudad)['text'] == "":
                ttk.Label(self.datos, text="Debe seleccionar una fila a modificar").grid(column=0, row=1)
            else:
                ttk.Label(self.datos, text="Ciudad:").grid(column=0, row=1)
                ttk.Label(self.datos, text="Codigo Postal:").grid(column=0, row=2)
                self.ciudad = ttk.Entry(self.datos, text="")
                self.ciudad.grid(column=1, row=1, columnspan=2)
                self.ciudad.insert(END, self.treeview.item(idCiudad)['text'])
                self.codigoPostal = ttk.Entry(self.datos, text="")
                self.codigoPostal.grid(column=1, row=2, columnspan=2)
                self.codigoPostal.insert(END, self.treeview.item(idCiudad)['values'][0])
                self.errorCampo = ttk.Label(self.datos, text="")
                self.errorCampo.grid(column=0, row=4)
                ttk.Button(self.datos, text="Confirmar", command=lambda: self.modificar(idCiudad)).grid(row=3, column=0)
        except:
            ttk.Label(self.datos, text="Debe seleccionar una fila a modificar").grid(column=0, row=4)

    def modificar(self, idCiudad):
        try:
            self.errorCampo.grid_remove()
            self.errorCampo = ttk.Label(self.datos, text="")
            self.errorCampo.grid(column=0, row=4)
            ciudad = self.ciudad.get()
            cp = self.codigoPostal.get()
            if ciudad == "" or cp == "":
                self.errorCampo.config(text="Debe completar todos los campos")
            else:
                self.treeview.insert("", self.treeview.index(idCiudad)+1, text=ciudad, values=cp)
                self.treeview.delete(idCiudad)
                self.limpiarGrilla()
                ttk.Label(self.datos, text="Modificado").grid(column=0, row=4)
        except:
            ttk.Label(self.datos, text="Debe seleccionar una fila a modificar").grid(column=0, row=4)

    def baja(self):
        self.limpiarGrilla()
        try:
            idCiudad = self.treeview.focus()
            self.treeview.delete(idCiudad)
            ttk.Label(self.datos, text="Baja confirmada").grid(column=0, row=1)
        except:
            ttk.Label(self.datos, text="Debe seleccionar una fila a borrar").grid(column=0, row=1)

    def limpiarGrilla(self):
        self.datos.grid_remove()
        self.datos = Frame(self.app)
        self.datos.grid(row=2, column=0)

app = Application()
