## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Ciudades Argentinas")
        
        def fila_seleccionada(event):
            fila = event.widget.focus()
            

        self.treeview = ttk.Treeview(self, columns=("codigo_postal"))

        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("codigo_postal", text="Codigo Postal")
        self.treeview.column('codigo_postal', anchor='center')
        self.treeview.insert("", tk.END, text="Rosario",
                             values=("2000"))
        self.treeview.insert("", tk.END, text="Buenos Aires",
                             values=("1675"))
        self.treeview.insert("", tk.END, text="Salta",
                             values=("4400"))
        self.treeview.insert("", tk.END, text="Cordoba",
                             values=("5000"))
        self.treeview.insert("", tk.END, text="Parana",
                             values=("3100"))
        self.treeview.pack()
        self.pack()
        self.treeview.bind('<<TreeviewSelect>>', fila_seleccionada)

        

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
