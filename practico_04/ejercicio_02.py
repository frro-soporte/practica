from tkinter import *
  
expresion = "" 
  
  
def press(num): 
    global expresion 
    expresion = expresion + str(num)   
    ecuacion.set(expresion)  
  
def equalpress(): 
    try: 
        global expresion 
        total = str(eval(expresion))   
        ecuacion.set(total) 
        expresion = "" 
    except: 
        ecuacion.set(" error ") 
        expresion = "" 

def clear(): 
    global expresion 
    expresion = "" 
    ecuacion.set("") 
   

if __name__ == "__main__": 
    gui = Tk() 
    gui.configure(background="light gray")  
    gui.title("Calculadora") 
    gui.geometry("265x170")  
    ecuacion = StringVar() 
    campo_expresion = Entry(gui, textvariable=ecuacion) 
    campo_expresion.grid(columnspan=4, ipadx=70,ipady=10) 
    ecuacion.set('Ingrese su expresión') 
    boton1 = Button(gui, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=1, width=7) 
    boton1.grid(row=2, column=0)   
    boton2 = Button(gui, text=' 2 ', fg='black', bg='white', command=lambda: press(2), height=1, width=7) 
    boton2.grid(row=2, column=1)   
    boton3 = Button(gui, text=' 3 ', fg='black', bg='white', command=lambda: press(3), height=1, width=7) 
    boton3.grid(row=2, column=2)   
    boton4 = Button(gui, text=' 4 ', fg='black', bg='white', command=lambda: press(4), height=1, width=7) 
    boton4.grid(row=3, column=0)   
    boton5 = Button(gui, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=1, width=7) 
    boton5.grid(row=3, column=1)   
    boton6 = Button(gui, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=1, width=7) 
    boton6.grid(row=3, column=2)   
    boton7 = Button(gui, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=1, width=7) 
    boton7.grid(row=4, column=0)   
    boton8 = Button(gui, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=1, width=7) 
    boton8.grid(row=4, column=1)   
    boton9 = Button(gui, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=1, width=7) 
    boton9.grid(row=4, column=2)   
    boton0 = Button(gui, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=1, width=7) 
    boton0.grid(row=5, column=0)   
    mas = Button(gui, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=1, width=7) 
    mas.grid(row=2, column=3)   
    menos = Button(gui, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=1, width=7) 
    menos.grid(row=3, column=3)   
    multiplicar = Button(gui, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=1, width=7) 
    multiplicar.grid(row=4, column=3)   
    dividir = Button(gui, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=1, width=7) 
    dividir.grid(row=5, column=3)   
    igual = Button(gui, text=' = ', fg='black', bg='white', command=equalpress, height=1, width=7) 
    igual.grid(row=5, column=2)   
    clear = Button(gui, text='Clear', fg='black', bg='white', command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
  
    
    gui.mainloop()