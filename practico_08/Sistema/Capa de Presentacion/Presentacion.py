import os
import flask
import sys
sys.path.append('c:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Datos')

from Metodos import DatosCiudades, DatosSacerdotes, DatosCentros
from flask import Flask, redirect, url_for, render_template, request, session, flash, send_from_directory
from datetime import timedelta, datetime
from flask_wtf import FlaskForm
from wtforms import SelectField


app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=60)


class Controles(FlaskForm):
    ddlciudades = SelectField('ddlciudades', choices=[])
    ddlCentros = SelectField('ddlCentros', choices=[])
    ddlSacerdotes = SelectField('ddlSacerdotes', choices=[])

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
    image_names = os.listdir('C:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/sacerdotes')
    ds = DatosSacerdotes()
    sacerdotes = ds.GetAll()
    for s in sacerdotes:
        s.centrosyDisponibilidad = ds.GetCentrosyHorarios(s)
    return render_template('sacerdotes.html', image_names=image_names, sacerdotes = sacerdotes)

@app.route('/centros')
def centro():
    image_names = os.listdir('C:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/centros')
    dc = DatosCentros()
    centros = dc.GetAll()
    for c in centros:
        c.sacerdotesyDisponibilidad = dc.GetSacerdotesyHorarios(c)
    return render_template('centros.html', image_names=image_names, centros = centros)

@app.route('/cancelarTurno')
def cancelarTurno():
    return render_template('cancelarTurno.html')

@app.route('/turnoSacerdote/<int:idSacerdote>') 
def turnoSacerdote(idSacerdote):
    ds = DatosSacerdotes()
    sacerdote = ds.GetOne(idSacerdote)
    rutaImagen = sacerdote.apellidoNombre.replace(", ", "") + ".png"
    sacerdote.centrosyDisponibilidad = ds.GetCentrosyHorarios(sacerdote)

    dc = DatosCentros()
    form = Controles()
    form.ddlCentros.choices = [(centro.idCentro, centro.nombre + " , " + centro.direccion) for centro in dc.GetAll()]
    return render_template('turnoSacerdote.html', image_name = rutaImagen, sacerdote = sacerdote, form = form)

@app.route('/turnoCentro/<int:idCentro>')
def turnoCentro(idCentro):
    dc = DatosCentros()
    centro = dc.GetOne(idCentro)
    rutaImangen = centro.nombre.replace(" ", "") + ".png"
    centro.sacerdotesyDisponibilidad = dc.GetSacerdotesyHorarios(centro)

    ds = DatosSacerdotes()
    form = Controles()
    form.ddlSacerdotes.choices = [(sacerdote.idSacerdote, sacerdote.apellidoNombre) for sacerdote in ds.GetAll()]
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

if __name__ == '__main__':
    app.run(debug=True)