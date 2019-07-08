import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


c = 0
root = tk.Tk()
root.title("Ciudades Argentinas")

tree=ttk.Treeview()
tree['columns']=('Ciudad','CP')
tree['show'] = 'headings'
tree.column('Ciudad', width=270, minwidth=270, stretch=tk.NO)
tree.column('CP', width=150, minwidth=150, stretch=tk.NO)

tree.heading('Ciudad',text="Ciudad",anchor=tk.W)
tree.heading('CP', text="Código Postal",anchor=tk.W)

tree.insert("", 1, text="", values=("Rosario","S2000"))
tree.insert("", 2, text="", values=("Pueblo Esther","S2129"))
tree.insert("", 3, text="", values=("Embalse","X5856"))
tree.insert("", 4, text="", values=("Colonia Alemana","X5196"))
tree.insert("", 5, text="", values=("Chabás","S2173"))
tree.insert("", 6, text="", values=("Casilda","S2170"))
tree.insert("", 7, text="", values=("Villa Constitución","S2919"))
tree.grid(row=2,columnspan=3)


def Funciones_alta(nomCiudad,cpCiudad,win):
    if (nomCiudad.get()=="" or cpCiudad.get()==""):
        messagebox.showinfo("Campos vacios","Debe completar todos los campos.")
    else:
        tree.insert("", tk.END, text="", values=(nomCiudad.get(),cpCiudad.get()))
    win.destroy()


def alta():
    win1 =tk.Tk()
    win1.title('Alta de Ciudad')
    back = tk.Frame(master=win1, width=250, height=15)
    back.pack()
    tk.Label(win1,text="Ciudad:").pack()
    nomCiudad = tk.Entry(win1, width=35)
    nomCiudad.pack()
    tk.Label(win1,text="Código Postal:").pack()
    cpCiudad = tk.Entry(win1, width=35)
    cpCiudad.pack()
    tk.Button(win1,text="Aceptar",command=lambda:Funciones_alta(nomCiudad, cpCiudad, win1)).pack()


def baja():
    items = tree.selection()
    print(items)
    if len(items)==0:
        messagebox.showinfo("No_Seleccion","Debe seleccionar items para eliminarlos.")
    else:
        for item in items:
            tree.delete(item)

def Funciones_modif(nomCiudad, cpCiudad, win, item):
    if (nomCiudad.get()=="" or cpCiudad.get()==""):
        messagebox.showinfo("Campos vacios","Debe completar todos los campos.")
    else:
        tree.set(item,'0',nomCiudad.get())
        tree.set(item,'1',cpCiudad.get())
    win.destroy()


def modif():
    item = tree.selection()
    if len(item) == 0:
        messagebox.showinfo("Ninguna Seleccion", "Debe seleccionar items para modificarlos.")
    elif len(item) > 1:
        messagebox.showinfo("Demasiadas Selecciones","Solo puede seleccionar un item para modificar.")
    else:
        win1 = tk.Tk()
        win1.title('Modificación Ciudad.')
        back = tk.Frame(master=win1, width=300, height=15)
        back.pack()
        tk.Label(win1,text="Ciudad Modificada:").pack()
        nomCiudad = tk.Entry(win1, width=45)
        nomCiudad.pack()
        nomCiudad.insert(0, tree.set(item,'0'))
        tk.Label(win1,text="Código Postal Modificado:").pack()
        cpCiudad = tk.Entry(win1, width=45)
        cpCiudad.insert(0, str(tree.set(item,'1')))
        cpCiudad.pack()
        tk.Button(win1,text="Aceptar",command=lambda:Funciones_modif(nomCiudad, cpCiudad, win1, item),width=25).pack()
        tk.Button(win1,text="Cancelar",command=lambda:win1.destroy(),width=25).pack()



marco_botones = tk.Frame(root,relief='sunken')
marco_botones.grid(row=0,columnspan=3,rowspan=1)
tk.Button(marco_botones,text="Alta",command=alta).grid(ipadx=15,ipady=5,row=0,padx=20,pady=20,column=0)
tk.Button(marco_botones,text="Baja",command=baja).grid(ipadx=15,ipady=5,row=0,padx=20,pady=20,column=1)
tk.Button(marco_botones,text="Modificación",command=modif).grid(ipadx=10,ipady=5,row=0,padx=20,pady=20,column=2)


root.mainloop()
