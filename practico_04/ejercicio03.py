## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 
from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Ciudades")
treeview = ttk.Treeview(ventana)

treeview.insert("",END, text = "Rosario 2000")
treeview.insert("",END, text ="Mendoza 5500")
treeview.insert("",END, text = "La Plata 1900")
treeview.insert("",END, text = "Cordoba 5000")
treeview.insert("",END, text = "Corrientes 3400")


treeview.pack()

ventana.mainloop()
