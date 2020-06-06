## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

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
        ttk.Label(frame, text="Valor 1").grid(column=1, row=1)
        ttk.Label(frame, text="Valor 2").grid(column=4, row=1)
        ttk.Label(frame, text="=").grid(column=6, row=1)
        ttk.Button(frame, text="+", command=self.sumar).grid(column=3, row=1)
        ttk.Button(frame, text="-", command=self.restar).grid(column=3, row=2)
        ttk.Button(frame, text="*", command=self.multiplicar).grid(column=3, row=3)
        ttk.Button(frame, text="/", command=self.dividir).grid(column=3, row=4)
        self.entrada1_texto = Entry(frame, width=10, textvariable="")
        self.entrada1_texto.grid(column=2, row=1)

        self.entrada2_texto = Entry(frame, width=10, textvariable="")
        self.entrada2_texto.grid(column=5, row=1)

        self.resultado = ttk.Label(frame, text="")
        self.resultado.grid(column=7, row=1)

    def sumar(self):
        try:
            _valor1 = float(self.entrada1_texto.get())
            _valor2 = float(self.entrada2_texto.get())
            _valor = _valor1 + _valor2
        except ValueError:
            _valor = "ERROR. Debe ingrese un numero"
        self.set_resultado(_valor)

    def restar(self):
        try:
            _valor1 = float(self.entrada1_texto.get())
            _valor2 = float(self.entrada2_texto.get())
            _valor = _valor1 - _valor2
        except ValueError:
            _valor = "ERROR. Debe ingrese un numero"
        self.set_resultado(_valor)

    def multiplicar(self):
        try:
            _valor1 = float(self.entrada1_texto.get())
            _valor2 = float(self.entrada2_texto.get())
            _valor = _valor1 * _valor2
        except ValueError:
            _valor = "ERROR. Debe ingrese un numero"
        self.set_resultado(_valor)

    def dividir(self):
        try:
            _valor1 = float(self.entrada1_texto.get())
            _valor2 = float(self.entrada2_texto.get())
            _valor = _valor1 / _valor2
        except ValueError:
            _valor = "ERROR. Debe ingrese un numero"
        self.set_resultado(_valor)

    def set_resultado(self, valor):
        self.resultado.grid_remove()
        self.resultado.grid(column=7, row=1)
        self.resultado.config(text=valor)


applicatcion = App()
