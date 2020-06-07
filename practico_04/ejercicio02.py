## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 


from tkinter import *
from tkinter import ttk


class App:
    def __init__(self):
        self.app = Tk()
        self.app.title("Calcuadora")
        self.crear_app()
        self.app.mainloop()

    def crear_app(self):
        frame = Frame(self.app)
        frame.grid(column=0, row=0)
        self.entrada_texto = ttk.Entry(frame, text="")
        self.entrada_texto.grid(column=0, row=0, columnspan=2)
        ttk.Button(frame, text="0", command=lambda: self.agregardigito("0")).grid(column=0, row=4)
        ttk.Button(frame, text="1", command=lambda: self.agregardigito("1")).grid(column=0, row=3)
        ttk.Button(frame, text="2", command=lambda: self.agregardigito("2")).grid(column=1, row=3)
        ttk.Button(frame, text="3", command=lambda: self.agregardigito("3")).grid(column=2, row=3)
        ttk.Button(frame, text="4", command=lambda: self.agregardigito("4")).grid(column=0, row=2)
        ttk.Button(frame, text="5", command=lambda: self.agregardigito("5")).grid(column=1, row=2)
        ttk.Button(frame, text="6", command=lambda: self.agregardigito("6")).grid(column=2, row=2)
        ttk.Button(frame, text="7", command=lambda: self.agregardigito("7")).grid(column=0, row=1)
        ttk.Button(frame, text="8", command=lambda: self.agregardigito("8")).grid(column=1, row=1)
        ttk.Button(frame, text="9", command=lambda: self.agregardigito("9")).grid(column=2, row=1)
        ttk.Button(frame, text="+", command=lambda: self.agregardigito("+")).grid(column=4, row=1)
        ttk.Button(frame, text="-", command=lambda: self.agregardigito("-")).grid(column=4, row=2)
        ttk.Button(frame, text="*", command=lambda: self.agregardigito("*")).grid(column=4, row=3)
        ttk.Button(frame, text="/", command=lambda: self.agregardigito("/")).grid(column=4, row=4)
        ttk.Button(frame, text="=", command=self.total, width=16).grid(column=1, row=4, columnspan=2)
        ttk.Button(frame, text="LIMPIAR", command=lambda: self.entrada_texto.delete(0, END)).grid(column=5, row=0)
        ttk.Label(frame, text="=").grid(column=2, row=0)
        self.resultado = ttk.Label(frame, text="")
        self.resultado.grid(column=4, row=0)

    def agregardigito(self, digito):
        self.entrada_texto.insert(len(self.entrada_texto.get()), digito)

    def total(self):
        try:
            _valor = eval(self.entrada_texto.get())
        except:
            _valor = "ERROR. Debe ingrese una expresion valida"
        self.resultado.grid_remove()
        self.resultado.grid(column=4, row=0)
        self.resultado.config(text=_valor)


applicatcion = App()
