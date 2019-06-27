## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 

import tkinter as tk
from tkinter import ttk

class Aplicacion(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Ciudades Argentinas")

        def fila_selec(event):
            fila = event.widget.focus()

        self.treeview = ttk.Treeview(self, columns=("CodigoPostal"))

        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("CodigoPostal", text="Codigo Postal")
        self.treeview.column('CodigoPostal', anchor='center')

        self.treeview.insert("", tk.END, text="Rosario",                values=("2000"))
        self.treeview.insert("", tk.END, text="Parana",                 values=("3100"))
        self.treeview.insert("", tk.END, text="La Plata",               values=("1900"))
        self.treeview.insert("", tk.END, text="Cordoba",                values=("5000"))
        self.treeview.insert("", tk.END, text="San Miguel de Tucuman",  values=("4000"))
        self.treeview.pack()
        self.pack()
        self.treeview.bind('<<TreeviewSelect>>', fila_selec)

main_window = tk.Tk()
app = Aplicacion(main_window)
app.mainloop()
