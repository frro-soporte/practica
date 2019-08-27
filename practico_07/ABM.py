import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Capa_negocio import NegocioSocio
from Capa_datos import Socio

c = 0
root = tk.Tk()
root.title("ABM Socios")

tree = ttk.Treeview()
tree['columns'] = ('ID', 'Nombre', 'Apellido', 'DNI')
tree['show'] = 'headings'
tree['selectmode'] = 'browse'
tree.column('ID', width=100, minwidth=270, stretch=tk.NO)
tree.column('Nombre', width=150, minwidth=150, stretch=tk.NO)
tree.column('Apellido', width=150, minwidth=150, stretch=tk.NO)
tree.column('DNI', width=150, minwidth=150, stretch=tk.NO)

tree.heading('ID', text="ID", anchor=tk.W)
tree.heading('Nombre', text="Nombre", anchor=tk.W)
tree.heading('Apellido', text="Apellido", anchor=tk.W)
tree.heading('DNI', text="DNI", anchor=tk.W)

cn = NegocioSocio()


def Refrescar(cn, tree):
    tree.delete(*tree.get_children())
    lista = cn.todos()
    if len(lista) != 0:
        for l in lista:
            tree.insert("", 1, text="", values=(l[0], l[2], l[3], l[1]))

    l = [(tree.set(k, 0), k) for k in tree.get_children('')]
    l.sort(reverse=False)
    for index, (val, k) in enumerate(l):
        tree.move(k, '', index)
    tree.grid()


Refrescar(cn, tree)


def Funciones_alta(dni, nombre, apellido, cn, win, tree, id):
    socio = Socio(dni=int(dni.get()), nombre=nombre.get(), apellido=apellido.get(), id=id.get())
    if (socio.dni is None or socio.nombre == "" or socio.apellido == ""):
        messagebox.showinfo("Campos vacios", "Debe completar todos los campos.")
    else:
        cn.alta(socio, win)
        Refrescar(cn, tree)
    win.destroy()


def alta(cn, tree):
    win1 = tk.Tk()
    win1.title('Alta de Socio')
    back = tk.Frame(master=win1, width=250, height=15)
    back.pack()
    child_id = tree.get_children()[-1]
    tk.Label(win1, text="ID:").pack()
    id = tk.Entry(win1, width=35)
    id.insert(0, int(tree.set(child_id, '0'))+1)
    id.configure(state='readonly')
    id.pack()
    tk.Label(win1, text="Nombre:").pack()
    nombre = tk.Entry(win1, width=35)
    nombre.pack()
    tk.Label(win1, text="Apellido:").pack()
    apellido = tk.Entry(win1, width=35)
    apellido.pack()
    tk.Label(win1, text="DNI:").pack()
    dni = tk.Entry(win1, width=35)
    dni.pack()
    tk.Button(win1, text="Aceptar", command=lambda: Funciones_alta(dni, nombre, apellido, cn, win1, tree, id), width=25).pack()
    tk.Button(win1, text="Cancelar", command=lambda: win1.destroy(), width=25).pack()



def baja(cn, tree):
    items = tree.focus()
    if len(items) == 0:
        messagebox.showinfo("No Seleccion", "Debe seleccionar items para eliminarlos.")
    else:
        if messagebox.askyesno("Baja Socio", "Seguro que desea eliminar el socio?"):
            cn.baja(tree.item(items)['values'][0])
            Refrescar(cn, tree)


def Funciones_modif(nombre, apellido, dni, win, cn, tree, id):
    socio = Socio(dni=int(dni.get()), nombre=nombre.get(), apellido=apellido.get(), id=id)
    if (socio.dni is None or socio.nombre == "" or socio.apellido == ""):
        messagebox.showinfo("Campos vacios", "Debe completar todos los campos.")
    else:
        cn.modificacion(socio, win)
        Refrescar(cn, tree)
    win.destroy()


def modif(cn, tree):
    item = tree.selection()
    if len(item) == 0:
        messagebox.showinfo("Ninguna Seleccion", "Debe seleccionar items para modificarlos.")
    else:
        win1 = tk.Tk()
        win1.title('Modificación Socio.')
        back = tk.Frame(master=win1, width=300, height=15)
        back.pack()
        tk.Label(win1, text="ID:").pack()
        id = tk.Entry(win1, width=45)
        id.insert(0, tree.set(item, '0'))
        id.configure(state='readonly')
        id.pack()
        tk.Label(win1, text="Nombre:").pack()
        nombre = tk.Entry(win1, width=45)
        nombre.pack()
        nombre.insert(0, tree.set(item, '1'))
        tk.Label(win1, text="Apellido:").pack()
        apellido = tk.Entry(win1, width=45)
        apellido.insert(0, str(tree.set(item, '2')))
        apellido.pack()
        tk.Label(win1, text="DNI:").pack()
        dni = tk.Entry(win1, width=45)
        dni.insert(0, str(tree.set(item, '3')))
        dni.pack()
        tk.Button(win1, text="Aceptar",
                  command=lambda: Funciones_modif(nombre, apellido, dni, win1, cn, tree, tree.set(item, '0')),
                  width=25).pack()
        tk.Button(win1, text="Cancelar", command=lambda: win1.destroy(), width=25).pack()


marco_botones = tk.Frame(root, relief='sunken')
marco_botones.grid(row=cn.MAX_SOCIOS, columnspan=3, rowspan=1)
tk.Button(marco_botones, text="Alta", command=lambda: alta(cn, tree)).grid(ipadx=15, ipady=5, row=10, padx=20, pady=20,
                                                                           column=0)
tk.Button(marco_botones, text="Baja", command=lambda: baja(cn, tree)).grid(ipadx=15, ipady=5, row=10, padx=20, pady=20,
                                                                           column=1)
tk.Button(marco_botones, text="Modificación", command=lambda: modif(cn, tree)).grid(ipadx=10, ipady=5, row=10, padx=20,
                                                                                    pady=20, column=2)

root.mainloop()
