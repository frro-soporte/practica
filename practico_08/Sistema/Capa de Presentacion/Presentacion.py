import os
import flask
import sys
# sys.path.append('c:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Datos')
sys.path.append('C:/Users/arias/Desktop/UTN/SGDPV/frro-soporte-2020-23/practico_08/Sistema/Capa de Datos')

from Metodos import DatosPenitentes, DatosCiudades, DatosSacerdotes, DatosCentros, DatosTurnos
from flask import Flask, redirect, url_for, render_template, request, session, flash, send_from_directory, jsonify
from datetime import timedelta, datetime
from flask_wtf import FlaskForm
from wtforms import SelectField
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=60)

### Configuracion FlaskMail ###
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'turnosconfesiones@gmail.com'
app.config['MAIL_PASSWORD'] = 'sgdpv2020'
app.config['MAIL_DEFAULT_SENDER'] = 'turnosconfesiones@gmail.com'
app.config['MAIL_ASCII_ATTACHMENTS'] = False
# app.config['DEBUG'] = True
# app.config['MAIL_DEBUG'] = True
# app.config['MAIL_SUPPRESS_SEND'] = False
# app.config['MAIL_DEFAULT_SENDER'] = 'turnosconfesiones@gmail.com'
mail = Mail(app)

class Controles(FlaskForm):
    ddlciudades = SelectField('ddlciudades', choices=[])
    ddlCentros = SelectField('ddlCentros', choices=[])
    ddlSacerdotes = SelectField('ddlSacerdotes', choices=[])
    ddlDias = SelectField('ddlDias', choices = [])
    ddlTurnos = SelectField('ddlTurnos', choices = [])

@app.route('/', methods=['GET'])
def home():
    dc = DatosCiudades()
    form = Controles()
    form.ddlciudades.choices = [(ciudad.idCiudad, ciudad.nombre + " , "+ciudad.provincia) for ciudad in dc.getAll()]
    
    return render_template('index.html', form=form)

@app.route('/upload/<filename>/<tipo>')
def send_image(filename,tipo):
    if(tipo == '1'):
        return send_from_directory("images/sacerdotes", filename)
    elif(tipo == '2'):
        return send_from_directory("images/centros", filename)


@app.route('/sacerdotes')
def sacerdotes():
    # image_names = os.listdir('C:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/sacerdotes')
    image_names = os.listdir('C:/Users/arias/Desktop/UTN/SGDPV/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/sacerdotes')
    ds = DatosSacerdotes()
    sacerdotes = ds.GetAll()
    for s in sacerdotes:
        s.centrosyDisponibilidad = ds.GetCentrosyHorarios(s)
    return render_template('sacerdotes.html', image_names=image_names, sacerdotes = sacerdotes)

@app.route('/centros')
def centro():
    # image_names = os.listdir('C:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/centros')
    image_names = os.listdir('C:/Users/arias/Desktop/UTN/SGDPV/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/sacerdotes')
    dc = DatosCentros()
    centros = dc.GetAll()
    for c in centros:
        c.sacerdotesyDisponibilidad = dc.GetSacerdotesyHorarios(c)
    return render_template('centros.html', image_names=image_names, centros = centros)

# @app.route('/cancelarTurno')
# def cancelarTurno():
#     return render_template('cancelarTurno.html')

@app.route('/turnoSacerdote/<int:idSacerdote>') 
def turnoSacerdote(idSacerdote):
    ds = DatosSacerdotes()
    sacerdote = ds.GetOne(idSacerdote)
    rutaImagen = sacerdote.apellidoNombre.replace(", ", "") + ".png"
    sacerdote.centrosyDisponibilidad = ds.GetCentrosyHorarios(sacerdote)

    dc = DatosCentros()
    form = Controles()
    form.ddlCentros.choices = [(centro.idCentro, centro.nombre + " , " + centro.direccion) for centro in dc.GetAllxSacerdote(sacerdote.idSacerdote)]
    #[(dia.nro, dia.desc) for dia in dt.GetDiasDisponiblesxSacerdoteyCentro(sacerdote.idSacerdote,)]
    return render_template('turnoSacerdote.html', image_name = rutaImagen, sacerdote = sacerdote, form = form)

@app.route('/diasDisponiblesxSacerdoteyCentro/<int:idSacerdote>/<int:idCentro>')
def getDiasDisponiblesxCentro (idSacerdote, idCentro):
    dt = DatosTurnos()
    
    diasLista = dt.GetDiasDisponiblesxSacerdoteyCentro(idSacerdote, idCentro)
    diasListaDict = []
    for dia in diasLista:
        diaDict = {}
        diaDict['id']=dia[0]
        diaDict['desc']=dia[1]
        diasListaDict.append(diaDict)
    
    return jsonify({'dias': diasListaDict})


@app.route('/turnoCentro/<int:idCentro>')
def turnoCentro(idCentro):
    dc = DatosCentros()
    centro = dc.GetOne(idCentro)
    rutaImangen = centro.nombre.replace(" ", "") + ".png"
    centro.sacerdotesyDisponibilidad = dc.GetSacerdotesyHorarios(centro)

    ds = DatosSacerdotes()
    form = Controles()
    form.ddlSacerdotes.choices = [(sacerdote.idSacerdote, sacerdote.apellidoNombre) for sacerdote in ds.GetAllxCentro(centro.idCentro)]
    form.ddlDias.choices = []
    form.ddlTurnos.choices = []
    return render_template('turnoCentro.html', image_name= rutaImangen, centro = centro, form=form)


@app.route('/logout')
def logout(): 
    flash('You have been logged out', 'info')
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

# Lo de abajo puede ser una funcion en la capa de metodos
# @app.route('/envioMail', methods=["POST", "GET"])
# def envioMail():
#     if request.method == "POST":
#         mail = request.form["mail"]
#         idTurno = request.form["idTurno"]
#         estado = request.form["estado"]
#         print('mail: ' + mail) 
#         print('idTurno' + idTurno)
#         print('estado' + estado) 
#         return render_template("confirmarTurno.html")
#     else:
#         return render_template("envioMail.html")

# obtener datos de un turno
def datosDeTurno(idTurno):
    dt = DatosTurnos()
    turno = dt.GetOne(idTurno)

    dc = DatosCentros()
    centro = dc.GetOne(turno.idCentro)

    ds = DatosSacerdotes()
    sacerdote = ds.GetOne(turno.idSacerdote)

    dp = DatosPenitentes()
    penitente = dp.searchByEmail(turno.mail)

    # print(turno.idTurno)
    # print(centro.nombre)
    # print(sacerdote.apellidoNombre)
    # print(penitente.nombreApellido)  
    return centro.nombre, sacerdote.apellidoNombre, penitente.mail

@app.route('/enviarMail')
def enviarMail():
    msg = Message('Hey there', recipients=['ariasramirox@gmail.com'])
    msg.html = '''<b> Prueba de html</b>
    <a href="http://127.0.0.1:5000/confirmarTurno">Confirmar turno</a>
    '''
    mail.send(msg)
    return 'Mail enviado'

# Esto tendria que ser cambiado para no manejar ids a la vista de la gente
@app.route('/confirmarTurno/', defaults={'idTurno' : 0})
@app.route('/confirmarTurno/<int:idTurno>')
def confirmarTurno(idTurno):
    dt = DatosTurnos()
    turno = dt.GetOne(idTurno) 
    if ( turno == None):
        return redirect(url_for('login'))   
    # falta manejo de exceptions en caso de que falle el ConfirmarTurno
    dt.ConfirmarTurno(idTurno)
    centroNombre, sacerdoteNombre, mail = datosDeTurno(idTurno)
    return render_template('confirmarTurno.html', centroNombre = centroNombre, sacerdoteNombre = sacerdoteNombre, mail=mail)



@app.route('/cancelarTurno/', defaults={'idTurno' : 0})
@app.route('/cancelarTurno/<int:idTurno>')
def cancelarTurno(idTurno):
    dt = DatosTurnos()
    turno = dt.GetOne(idTurno) 
    if ( turno == None):
        return redirect(url_for('login'))   
    # falta manejo de exceptions en caso de que falle el CancelarTurno
    dt.CancelarTurno(idTurno)
    centroNombre, sacerdoteNombre, mail = datosDeTurno(idTurno)
    return render_template('cancelarTurno.html', centroNombre = centroNombre, sacerdoteNombre = sacerdoteNombre, mail=mail)


if __name__ == '__main__':   
    app.run(debug=True)