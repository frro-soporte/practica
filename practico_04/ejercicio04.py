## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 



import tkinter as tk
from tkinter import ttk
from tkinter import *
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Ciudades Argentinas")
        
        def fila_seleccionada(event):
                self.valor_1_txt.delete(0,END)            
                self.valor_2_txt.delete(0,END)
                global row_selected
                self.fila = event.widget.focus()
                self.values = event.widget.item(self.fila)['values']
                self.valor_1_txt.insert(0,self.values[0])
                self.valor_2_txt.insert(0,self.values[1])

        def agregar_ciudad():
                """
                Insertion method.
                """
                self.tree.insert('', 'end',values=(self.valor_1_txt.get(), self.valor_2_txt.get()))
                # Increment counter
                self.valor_1_txt.delete(0,END)            
                self.valor_2_txt.delete(0,END)
        
        def borrar_ciudad():
                self.tree.delete(self.fila)
                self.valor_1_txt.delete(0,END)            
                self.valor_2_txt.delete(0,END)
                
        self.DATA = [('ROSARIO', '2000'),
        ('CORDOBA', '5000'),
        ('BUENOS AIRES', '1675'),
        ('SALTA', '4400'),
        ('PARANA', '3100'),
        ]


        self.header = ('Ciudad', 'Codigo Postal')
        self.label1 =Label(ventana,  text ="Ciudad")
        self.valor_1_txt =Entry(ventana, width=20)
        self.label1.grid(row = 1, column = 0)
        self.valor_1_txt.grid(row = 1, column = 1)
        self.label2 =Label(ventana, text ="Codigo Postal")
        self.valor_2_txt =Entry(ventana,width=6)
        self.label2.grid(row = 2, column = 0)
        self.valor_2_txt.grid(row = 2, column = 1)

        self.boton_agregar = Button(text = "Insertar Ciudad", command = agregar_ciudad)
        self.boton_agregar.grid(row = 3, column = 1)
        self.boton_borrar = Button(text = "Borrar Ciudad", command = borrar_ciudad)
        self.boton_borrar.grid(row = 3, column = 3)

        self.tree = ttk.Treeview(columns=self.header,
                            show="headings",
                            height=5)
        self.tree.grid(row=4, columnspan=4,sticky='nsew' )
        for col, text in enumerate(self.header):
            self.tree.heading(col, text=text)
        self.tree.bind('<<TreeviewSelect>>', fila_seleccionada)

        for record in self.DATA:
            self.tree.insert('', 'end', values=record)


ventana = tk.Tk()
ventana.title('Ciudades')
app = Application(ventana)
app.mainloop()



