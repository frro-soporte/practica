## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra ventana donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 



import tkinter as tk
from tkinter import ttk
from tkinter import *

ventana = tk.Tk()
ventana.title('Ciudades')

DATA = [('ROSARIO', '2000'),
        ('CORDOBA', '5000'),
        ('BUENOS AIRES', '1675'),
        ('SALTA', '4400'),
        ('PARANA', '3100'),
        ]
def invoice_selected(event):
        valor_1_txt.delete(0,END)            
        valor_2_txt.delete(0,END)
        global row_selected
        row_selected = event.widget.focus()
        values = event.widget.item(row_selected)['values']
        valor_1_txt.insert(0,values[0])
        valor_2_txt.insert(0,values[1])

def agregar_ciudad():
        """
        Insertion method.
        """
        tree.insert('', 'end',values=(valor_1_txt.get(), valor_2_txt.get()))
        # Increment counter
        valor_1_txt.delete(0,END)            
        valor_2_txt.delete(0,END)

def borrar_ciudad():
        tree.delete(row_selected)
        valor_1_txt.delete(0,END)            
        valor_2_txt.delete(0,END)
        

header = ('Ciudad', 'Codigo Postal')
label1 =Label(ventana,  text ="Ciudad")
valor_1_txt =Entry(ventana, width=20)
label1.grid(row = 1, column = 0)
valor_1_txt.grid(row = 1, column = 1)
label2 =Label(ventana, text ="Codigo Postal")
valor_2_txt =Entry(ventana,width=6)
label2.grid(row = 2, column = 0)
valor_2_txt.grid(row = 2, column = 1)

boton_agregar = Button(text = "Insertar Ciudad", command = agregar_ciudad)
boton_agregar.grid(row = 3, column = 1)
boton_borrar = Button(text = "Borrar Ciudad", command = borrar_ciudad)
boton_borrar.grid(row = 3, column = 3)

tree = ttk.Treeview(columns=header,
                    show="headings",
                    height=5)
tree.grid(row=4, columnspan=4,sticky='nsew' )
for col, text in enumerate(header):
    tree.heading(col, text=text)
tree.bind('<<TreeviewSelect>>', invoice_selected)

for record in DATA:
    tree.insert('', 'end', values=record)

ventana.mainloop()

