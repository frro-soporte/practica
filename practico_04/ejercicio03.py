## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 
from tkinter import  *
from tkinter import ttk
import tkinter as tk

window = Tk()
window.title('Ciudades Argentinas')
arbol = ttk.Treeview()

arbol["columns"]=("one")

arbol.heading("#0",text="Ciudad")

# Level 1
rosario = arbol.insert("", tk.END, text="Rosario")
cordoba = arbol.insert("", tk.END, text="Cordoba")
salta = arbol.insert("", tk.END, text="Salta")
resistencia = arbol.insert("", tk.END, text="Resistencia")
sn = arbol.insert("", tk.END, text="San Nicolas")

# Level 2
arbol.insert(rosario, "end", text="2000")
arbol.insert(cordoba, "end", text="5000")
arbol.insert(salta, "end", text="4400")
arbol.insert(resistencia, "end", text="3500")
arbol.insert(sn, "end", text="2900")

arbol.grid()

window.mainloop()