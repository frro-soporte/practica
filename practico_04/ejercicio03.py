## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 


from tkinter import *
from tkinter import ttk


class Application:
    def __init__(self):
        self.app = Tk()
        self.app.title("Ciudades argentinas")
        self.frame = Frame(self.app)
        self.frame.grid(column=0, row=0)

        self.treeview = ttk.Treeview(self.frame)
        self.treeview["columns"] = "one"
        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("one", text="Codigo postal")
        self.treeview.pack()
        self.agregarciudad("rosario", "2000")
        self.agregarciudad("quilmes", "1879")
        self.agregarciudad("cordoba", "5000")
        self.agregarciudad("san rafael", "4000")
        self.agregarciudad("pehuajo", "5500")
        self.app.mainloop()

    def agregarciudad(self, nombre, codigo_postal):
        self.treeview.insert("", END, text=nombre, values=codigo_postal)


app = Application()

