import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ciudades Argentinas")
tree=ttk.Treeview()


tree["columns"]=("one")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)

tree.heading("#0",text="Ciudad",anchor=tk.W)
tree.heading("one", text="Código Postal",anchor=tk.W)

tree.insert("", 1, text="Rosario", values=("S2000"))
tree.insert("", 2, text="Pueblo Esther", values=("S2129"))
tree.insert("", 3, text="Embalse", values=("X5856"))
tree.insert("", 4, text="Colonia Alemana", values=("X5196"))
tree.insert("", 5, text="Chabás", values=("S2173"))
tree.insert("", 6, text="Casilda", values=("S2170"))
tree.insert("", 7, text="Villa Constitución", values=("S2919"))
tree.pack(side=tk.TOP,fill=tk.X)

ventana.mainloop()