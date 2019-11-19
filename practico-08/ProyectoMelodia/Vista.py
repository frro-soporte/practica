from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as msb
from Negocio import AbrirNegocio
import os

negocio = AbrirNegocio()


"""Metodos creadores de Ventanas"""


def AbreMenu():
    winMenu = Tk()
    winMenu.resizable(width=False, height=False)
    winMenu.title("Menu")

    C = Canvas(winMenu, bg="blue", height=350, width=600)
    backImage = PhotoImage(file=".\\Recursos\\Imagenes\\Fondo_Menu.png")
    background = Label(winMenu, image=backImage)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    btnGrabarImage = PhotoImage(file=".\\Recursos\\Iconos\\Microfono.png")
    btnGrabar = Button(winMenu, text="Grabar Nuevo Audio",bg="PaleTurquoise1" ,image=btnGrabarImage, compound="left", width=300,height=30, command= lambda: VentanaGrabar(winMenu)).place(x=15,y=250)

    btnAbrirImage = PhotoImage(file=".\\Recursos\\Iconos\\Carpeta.png")
    btnAbrir = Button(winMenu, text="Abrir Audio Existente", bg="PaleTurquoise1",image=btnAbrirImage, compound="left",width=300,height=30, command= lambda: VentanaAbrir(winMenu)).place(x=15, y=290)

    C.pack()
    winMenu.mainloop()


def AbreAbrirAudio():

    winAbrir = Tk()
    winAbrir.title("Abrir Audio")
    winAbrir.resizable(width=False, height=False)

    C = Canvas(winAbrir, bg="blue", height=350, width=600)
    backImage = PhotoImage(file=".\\Recursos\\Imagenes\\Fondo.png")
    background = Label(winAbrir, image=backImage)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()

    # Declaro el TreeView
    tree = ttk.Treeview(winAbrir)
    tree['columns'] = ('Nombre', 'Descripcion', 'Autor')
    tree['show'] = 'headings'
    tree['selectmode'] = 'browse'

    tree.column('Nombre', width=125, stretch=NO)
    tree.column('Descripcion', width=340, stretch=NO)
    tree.column('Autor', width=125, stretch=NO)

    tree.heading('Nombre', text="Nombre", anchor=W)
    tree.heading('Descripcion', text="Descripción", anchor=W)
    tree.heading('Autor', text="Autor", anchor=W)
    tree.pack()


    LoadTree(tree)

    # Creo los botones
    btnPlayImage = PhotoImage(file=".\\Recursos\\Iconos\\Play.png")
    btnPlay = Button(winAbrir, command=lambda: Play(tree), image=btnPlayImage).place(x=5, y=265)
    btnAbrir = Button(winAbrir, text="Abrir", width=11, height=2,bg="SteelBlue1", command=lambda: BtnAbreAnalisis(tree, winAbrir)).place(y=265, x=510)
    btnVolver = Button(winAbrir,bg="snow",text="Volver", width=11, command= lambda: Volver(winAbrir)).place(y=315, x=510)
    btnEditarImage = PhotoImage(file=".\\Recursos\\Iconos\\Editar.png")
    btnEditar = Button(winAbrir, image=btnEditarImage,bg="snow" ,command=lambda: Modificar(tree, winAbrir)).place(y=2,x=5)
    btnEliminarImage = PhotoImage(file=".\\Recursos\\Iconos\\Eliminar.png")
    btnEliminar = Button(winAbrir,bg="snow", command=lambda: Eliminar(tree), image=btnEliminarImage).place(y=2,x=35)
    winAbrir.mainloop()

def AbreEditar(txtNombre, txtDesc, txtAutor, tree):
    winEdit = Tk()
    winEdit.title("Editar Datos de Audio")
    winEdit.resizable(width=False, height=False)

    C = Canvas(winEdit, bg="blue", height=220, width=600)
    backImage = PhotoImage(file=".\\Recursos\\Imagenes\\Fondo.png")
    background = Label(winEdit, image=backImage)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()

    lblNombre = Label(winEdit, text="Nombre:").place(x=5, y=5)
    txtNombreE = Entry(winEdit, width=95)
    txtNombreE.insert(0, txtNombre)
    txtNombreE.configure(state='readonly')
    txtNombreE.place(x=5, y=30)

    lblDescripcion = Label(winEdit, text="Descripción:").place(x=5, y=55)
    txtDescripcionE = Entry(winEdit, width=95)
    txtDescripcionE.insert(0, txtDesc)
    txtDescripcionE.place(x=5, y=80)

    lblAutor = Label(winEdit, text="Autor:").place(x=5, y=105)
    txtAutorE = Entry(winEdit, width=95)
    txtAutorE.insert(0, txtAutor)
    txtAutorE.place(x=5, y=130)

    btnGuardar = Button(winEdit, text="Guardar", width=10, bg="SteelBlue1",
                        command=lambda: BtnGuardarEditar(winEdit, txtNombreE, txtAutorE, txtDescripcionE, tree)).place(y=170, x=500)
    btnCancelar = Button(winEdit, text="Cancelar", bg="snow",width=10, command=lambda: BtnCancelarEditar(winEdit)).place(y=170,
                                                                                                              x=400)

    winEdit.mainloop()

def AbreGrabar():
    winGrab = Tk()
    winGrab.title("Grabar Audio")
    winGrab.resizable(width=False, height=False)

    C = Canvas(winGrab, bg="blue", height=200, width=600)
    backImage = PhotoImage(file=".\\Recursos\\Imagenes\\Fondo.png")
    background = Label(winGrab, image=backImage)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()

    recordImage = PhotoImage(file=".\\Recursos\\Iconos\\Grabar.png")
    lblGraba = Label(winGrab, image=recordImage,bg="snow", borderwidth=2, relief="groove")
    lblGraba.place(x=5, y=5, relwidth=0.5, relheight=0.7)
    muteImage = PhotoImage(file=".\\Recursos\\Iconos\\NoMicro.png")
    lblMute = Label(winGrab, image=muteImage,bg="snow", borderwidth=2, relief="groove")
    lblMute.place(x=5, y=5, relwidth=0.5, relheight=0.7)

    lblTiempo = Label(winGrab, text="Ingrese el tiempo de grabación(seg)", borderwidth=2, relief="groove",bg="snow").place(x=110, y=150)
    txtTiempo = Entry(winGrab, width=15)
    txtTiempo.place(x=210, y=170)

    btnGrabarImg = PhotoImage(file=".\\Recursos\\Iconos\\Microfono.png")
    btnGrabar = Button(winGrab, image=btnGrabarImg, command=lambda: IniciaGrabacion(lblMute, recordImage, muteImage, txtTiempo, btnRep, txtNombre, txtDesc, txtAutor, btnAceptar, winGrab))
    btnGrabar.place(x=5, y=150)
    btnRepImg = PhotoImage(file=".\\Recursos\\Iconos\\Play.png")
    btnRep = Button(winGrab, image=btnRepImg, state=DISABLED, command=lambda: PlayGrabar())
    btnRep.place(x=50,y=150)

    lblNombre = Label(winGrab, text="Nombre:", bg="snow",borderwidth=2, relief="groove").place(y=5, x=320)
    txtNombre = Entry(winGrab, width=45, state=DISABLED)
    txtNombre.place(x=320, y=30)

    lblDesc = Label(winGrab, text="Descripción:", bg="snow",borderwidth=2, relief="groove").place(y=55, x=320)
    txtDesc = Entry(winGrab, width=45, state=DISABLED)
    txtDesc.place(x=320, y=79)

    lblAutor = Label(winGrab, text="Autor:", bg="snow",borderwidth=2, relief="groove").place(y=104, x=320)
    txtAutor = Entry(winGrab, width=45, state=DISABLED)
    txtAutor.place(x=320, y=128)

    btnCancelar = Button(winGrab, text="Cancelar",command= lambda: BtnCancelarGrabar(winGrab), bg="snow", width=11).place(y=170, x=410)
    btnAceptar = Button(winGrab, text="Aceptar", bg="SteelBlue1", state=DISABLED, width=11, command=lambda: BtnGuardarAudio(txtNombre, txtAutor,txtDesc,btnAceptar,btnRep,txtTiempo, winGrab))
    btnAceptar.place(y=170, x=507)

    winGrab.mainloop()

def AbreAnalisis(nombre):
    winAnalisis = Tk()
    winAnalisis.title("Análisis de Audios")
    winAnalisis.resizable(width=False, height=False)

    C = Canvas(winAnalisis, bg="blue", height=550, width=1010)
    backImage = PhotoImage(file=".\\Recursos\\Imagenes\\Fondo_Analisis.png")
    background = Label(winAnalisis, image=backImage)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()

    GeneraAnalisis(nombre)

    lblChromaTexto = Label(winAnalisis, text="Análisis del Audio: {0}.".format(nombre), borderwidth=2, relief="groove", bg="snow").place(x=5,y=5)
    imgChroma = PhotoImage(file=".\\CapaDatos\\Graphics\\{0}_Chroma.png".format(nombre))
    lblChroma = Label(winAnalisis, image=imgChroma, borderwidth=2, relief="groove").place(y=30, x=5)


    lblAudioOriginal = Label(winAnalisis, text="Audio de la Grabación Original: ", borderwidth=2, relief="groove", bg="snow").place(y=460, x=5)
    imgAudio = PhotoImage(file=".\\Recursos\\Iconos\\Play.png")
    btnAudioOriginal = Button(winAnalisis, text="Reproducir" , image = imgAudio, compound="left", command=lambda: AbrirAudioOrig(nombre)).place(y=490, x=5)

    lblAudioMel = Label(winAnalisis, text="Audio de la Melodía Generada: ", borderwidth=2, relief="groove",bg="snow").place(y=460, x=440)
    btnAudioMel = Button(winAnalisis, text="Reproducir", image = imgAudio, compound="left", command=lambda: AbrirAudioMel(nombre)).place(y=490,x=440)

    btnVolver = Button(winAnalisis, text="Volver", width=15, height=2, bg="SteelBlue1", command=lambda: Volver(winAnalisis)).place(y=490, x=892)


    winAnalisis.mainloop()

"""Metodos de Menu"""

def VentanaGrabar(winMenu):
    winMenu.destroy()
    AbreGrabar()

def VentanaAbrir(winMenu):
    winMenu.destroy()
    AbreAbrirAudio()

def Volver(winAbrir):
    winAbrir.destroy()
    AbreMenu()

"""Metodos de Analisis"""

def GeneraAnalisis(nombre):
    try:
        if not os.path.exists(".\\CapaDatos\\Songs\\{0}_Mel.wav".format(nombre)):
            negocio.GeneraAudioMelodia(nombre)
            negocio.GeneraChromagrama(nombre)
    except Exception as x:
        msb.showinfo("Error", x.args)

def AbrirAudioMel(nombre):
    try:
        negocio.Reproducir_Analisis_Mel(nombre)
    except Exception as x:
        msb.showinfo("Error", x.args)

def AbrirAudioOrig(nombre):
    try:
        negocio.Abrir_Reproducir(nombre)
    except Exception as x:
        msb.showinfo("Error", x.args)
        

"""Metodos de Grabar"""

def BtnCancelarGrabar(win):
    try:
        os.remove(".\\TKinter.wav")
    except:
        pass
    win.destroy()
    AbreMenu()

def BtnGuardarAudio(txtNom, txtAu, txtDesc, btnGuardar, btnPlay, txtTie, win):
    try:
        if len(txtNom.get()) == 0:
            raise Exception("El nombre del audio es un campo obligatorio.")
        negocio.GuardaAudio(txtNom.get(), txtAu.get(), txtDesc.get())
        msb.showinfo("Exito!","Audio guardado exitosamente.")
        nombre = txtNom.get()
        txtTie.delete(0, 'end')
        txtDesc.delete(0, 'end')
        txtAu.delete(0, 'end')
        txtNom.delete(0, 'end')
        btnPlay.configure(state=DISABLED)
        btnGuardar.configure(state=DISABLED)
        txtNom.configure(state=DISABLED)
        txtDesc.configure(state=DISABLED)
        txtAu.configure(state=DISABLED)
        if msb.askyesno("Analisis", "Desea abrir el análisis del audio grabado recientemente?"):
            win.destroy()
            AbreAnalisis(nombre)
    except Exception as x:
        msb.showinfo("Error", x.args)

def IniciaGrabacion(lbl, img, img1, txtTie, btn, txtNom, txtAu, txtDesc, btnGuar, win):
    try:
        if len(txtTie.get()) == 0:
            raise Exception("Debe ingresar tiempo de grabación")
        seconds = float(txtTie.get())
        lbl.configure(image=img)
        win.update()
        negocio.Grabar(seconds)
        msb.showinfo("Exito!","Grabación realizada correctamente.")
        lbl.configure(image=img1)
        win.update()
        btn.configure(state=NORMAL)
        btnGuar.configure(state=NORMAL)
        txtNom.configure(state=NORMAL)
        txtDesc.configure(state=NORMAL)
        txtAu.configure(state=NORMAL)
    except Exception as x:
        msb.showinfo("Error", x.args)

def PlayGrabar():
    try:
        negocio.Abrir_Reproducir("TKinter.wav")
    except Exception as x:
        msb.showinfo("Error", x.args)

"""Metodos de Abrir"""

def BtnAbreAnalisis(tree, win):
    try:
        itemActual = tree.focus()
        if len(itemActual) == 0:
            raise Exception("Debe seleccionar un audio abrir su análisis")
        nombre = tree.item(itemActual)['values'][0]
        win.destroy()
        AbreAnalisis(nombre)
    except Exception as x:
        msb.showinfo("Error", x.args)

def LoadTree(tree):
    try:
        tree.delete(*tree.get_children())
        songs = negocio.Lista_Audios()
        if len(songs) != 0:
            for s in songs:
                tree.insert("", 1, text="", values=(s[0], s[1], s[2]))
        tree.place(x=5, y=30)

    except Exception as x:
        msb.showinfo("Error", x.args)

def Eliminar(tree):
    try:
        itemActual = tree.focus()
        if len(itemActual) == 0:
            raise Exception("Debe seleccionar un audio para eliminarlo")
        else:
            if msb.askyesno("Baja Socio", "Seguro que desea eliminar el audio?"):
                nombre = tree.item(itemActual)['values'][0]
                negocio.Eliminar(nombre)
                LoadTree(tree)
    except Exception as x:
            msb.showinfo("Error", x.args)

def Modificar(tree, winAbrir):
    itemActual = tree.selection()
    try:
        if len(itemActual) == 0:
            raise Exception("Debe seleccionar un audio para modificarlo")
        else:
            tupla = (tree.item(itemActual)['values'][0], tree.item(itemActual)['values'][1],
                     tree.item(itemActual)['values'][2])
            winAbrir.destroy()
            AbreEditar(tupla[0], tupla[1], tupla[2], tree)
    except Exception as x:
        msb.showinfo("Error", x.args)

def Play(tree):
    try:
        itemActual = tree.focus()
        if len(itemActual) == 0:
            raise Exception("Debe seleccionar un audio para escucharlo.")
        else:
            nombre = tree.item(itemActual)['values'][0]
            negocio.Abrir_Reproducir(nombre)

    except Exception as x:
        msb.showinfo("Error", x.args)

"""Metodos Ventana Editar"""
def BtnGuardarEditar(winEdit,txtNombre, txtAutor, txtDescripcion, tree):
    try:
        negocio.Modifica(txtNombre.get(), txtAutor.get(), txtDescripcion.get())
        msb.showinfo("Edición Exitosa!", "El audio {0} se ha editado exitosamente".format(txtNombre.get()))
        winEdit.destroy()
        AbreAbrirAudio()
    except Exception as x:
        msb.showinfo("Error", x.args)

def BtnCancelarEditar(winEdit):
    winEdit.destroy()
    AbreAbrirAudio()


if __name__ == '__main__':
    AbreMenu()
