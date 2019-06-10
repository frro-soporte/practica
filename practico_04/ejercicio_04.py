# Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones
# 1- un  botón  Alta que inicia otra venta donde puedo ingresar una ciudad y su código postal .
# 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
# 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra .
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


main_window = tk.Tk()

class Form(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Ejercicio 03")
        main_window.geometry("400x320")

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







app = Form(main_window)

def alta():
    new_window = tk.Toplevel(main_window)
    var_ciudad = tk.StringVar()
    var_CP = tk.StringVar()
    label1 = tk.Label(new_window, text="Ciudad").place(x=10, y=10)
    label2 = tk.Label(new_window, text="Codigo postal").place(x=10, y=80)
    input1 = tk.Entry(new_window, textvariable=var_ciudad).place(x=10, y=40)
    input2 = tk.Entry(new_window, textvariable=var_CP).place(x=10, y=120)


    def insert():
        if (var_ciudad.get()) != '':
            app.treeview.insert("", tk.END, text=var_ciudad.get(), values=(var_CP.get()))
            new_window.iconify()
        else:
            messagebox.showerror("Error", "Los campos no pueden estar vacios")
            new_window.deiconify()

    button = tk.Button(new_window, text="Añadir", command=insert).place(x=50, y=150)
def baja():
    item = app.treeview.focus()
    app.treeview.delete(item)

def mod():
    new_window = tk.Toplevel(main_window)
    item = app.treeview.focus()

    var_ciudad = tk.StringVar(new_window, value= app.treeview.item(item)['text'])
    var_CP = tk.StringVar(new_window, value=app.treeview.set(item, "codp"))

    label1 = tk.Label(new_window, text="Ciudad").place(x=10, y=10)
    label2 = tk.Label(new_window, text="Codigo postal").place(x=10, y=80)
    input1 = tk.Entry(new_window, textvariable=var_ciudad).place(x=10, y=40)
    input2 = tk.Entry(new_window, textvariable=var_CP).place(x=10, y=120)

    def execute():
        if (var_ciudad.get()) != '':
            app.treeview.item(item, text=var_ciudad.get())
            app.treeview.item(item, values=var_CP.get())
            new_window.iconify()
        else:
            messagebox.showerror("Error", "Los campos no pueden estar vacios")
            new_window.deiconify()


    button = tk.Button(new_window, text="Añadir", command=execute).place(x=50, y=150)

btn_frm_mod = tk.Button(main_window, text="MODIFICACION", command=mod)
btn_frm_mod.pack(side = tk.RIGHT,padx=10)

btn_frm_baja = tk.Button(main_window, text="BAJA",command=baja)
btn_frm_baja.pack(side = tk.RIGHT,padx=10)

btn_frm_alta = tk.Button(main_window, text="ALTA",command=alta)
btn_frm_alta.pack(side=tk.RIGHT,padx=10)





app.mainloop()


