import os
import flask
import sys
sys.path.append('c:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Datos')

from Metodos import DatosCiudades, DatosSacerdotes, DatosCentros
from flask import Flask, redirect, url_for, render_template, request, session, flash, send_from_directory
from datetime import timedelta
from flask_wtf import FlaskForm
from wtforms import SelectField


app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=60)


class Home(FlaskForm):
    ddlciudades = SelectField('ddlciudades', choices=[])

@app.route('/', methods=['GET'])
def home():
    dc = DatosCiudades()
    form = Home()
    form.ddlciudades.choices = [(ciudad.idCiudad, ciudad.nombre) for ciudad in dc.getAll()]
    
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
    return render_template('sacerdotes.html', image_names=image_names, sacerdotes = sacerdotes)

@app.route('/centros')
def centro():
    dc = DatosCentros()
    centros = dc.GetAll()
    image_names = os.listdir('C:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/centros')
    return render_template('centros.html', image_names=image_names, centros = centros)

@app.route('/cancelarTurno')
def cancelarTurno():
    return render_template('cancelarTurno.html')

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