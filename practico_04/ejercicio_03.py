# Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
# Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) .

import tkinter as tk
from tkinter import ttk


class Form(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Ejercicio 03")
        main_window.geometry("350x150")

        self.treeview = ttk.Treeview(self)

        self.treeview = ttk.Treeview(self, columns=("codp"))

        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("codp", text="Codigo Postal")
        self.treeview.insert("", tk.END, text="Rosario",values=("2000"))
        self.treeview.insert("", tk.END, text="San José de la Esquina", values=("2185"))
        self.treeview.insert("", tk.END, text="Sunchales", values=("2322"))
        self.treeview.insert("", tk.END, text="Sunchales", values=("2300"))
        self.treeview.insert("", tk.END, text="Casilda", values=("2170"))

        self.treeview.pack()

        self.pack()


main_window = tk.Tk()
app = Form(main_window)
app.mainloop()