import os
import flask
import sys
sys.path.append('c:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Datos')
#sys.path.append('C:/Users/arias/Desktop/UTN/SGDPV/frro-soporte-2020-23/practico_08/Sistema/Capa de Datos')
# sys.path.append('/home/jco/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Datos')

from Clases import Turno
from Metodos import DatosPenitentes, DatosCiudades, DatosSacerdotes, DatosCentros, DatosTurnos
from flask import Flask, redirect, url_for, render_template, request, session, flash, send_from_directory, jsonify
from datetime import timedelta, datetime
from flask_wtf import FlaskForm
from wtforms import SelectField
from flask_mail import Mail, Message
from flask_login import LoginManager, login_required, current_user


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
FlaskMailApp = Mail(app)

login_manager = LoginManager()
# cuando alguien no esta autentuficado se redirige a login
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# flask-login will create a cookie when the user is logged in 
# inside the cookie will be de user_id
# everytime the user perform a request on the app its send the cookie along 
# the request, so flask-login looks in that cookie,looks for the user_id and
# takes that and use de load_user to actually find the user in the db
@login_manager.user_loader
# user_id es tomada de la cookie
def load_user(user_id):
    ds = DatosSacerdotes()
    sacerdote = ds.GetOne(user_id)
    return sacerdote

from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

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
    image_names = os.listdir('C:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/sacerdotes')
    #image_names = os.listdir('C:/Users/arias/Desktop/UTN/SGDPV/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/sacerdotes')
    # image_names = os.listdir('/home/jco/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/sacerdotes')
    ds = DatosSacerdotes()
    sacerdotes = ds.GetAll()
    for s in sacerdotes:
        s.centrosyDisponibilidad = ds.GetCentrosyHorarios(s)
    return render_template('sacerdotes.html', image_names=image_names, sacerdotes = sacerdotes)

@app.route('/centros')
def centro():
    image_names = os.listdir('C:/Users/ppaez/Documents/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/centros')
    # image_names = os.listdir('C:/Users/arias/Desktop/UTN/SGDPV/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/sacerdotes')
    # image_names = os.listdir('/home/jco/Repositorios/frro-soporte-2020-23/practico_08/Sistema/Capa de Presentacion/images/centros')
    dc = DatosCentros()
    centros = dc.GetAll()
    for c in centros:
        c.sacerdotesyDisponibilidad = dc.GetSacerdotesyHorarios(c)
    return render_template('centros.html', image_names=image_names, centros = centros)


@app.route('/turnoSacerdote/<int:idSacerdote>') 
def turnoSacerdote(idSacerdote):
    ds = DatosSacerdotes()
    sacerdote = ds.GetOne(idSacerdote)
    rutaImagen = sacerdote.apellidoNombre.replace(", ", "") + ".png"
    sacerdote.centrosyDisponibilidad = ds.GetCentrosyHorarios(sacerdote)

    dc = DatosCentros()
    dt = DatosTurnos()
    form = Controles()
    form.ddlCentros.choices = [(centro.idCentro, centro.nombre + " , " + centro.direccion) for centro in dc.GetAllxSacerdote(sacerdote.id)]
    form.ddlDias.choices = [(dia[0], dia[1]) for dia in dt.GetDiasDisponiblesxSacerdoteyCentro(idSacerdote, form.ddlCentros.choices[0][0])]
    form.ddlTurnos.choices = [(turno[0], turno[1]) for turno in dt.GetPeriodosDisponiblesxSacerdoteCentroyDia(idSacerdote, form.ddlCentros.choices[0][0], form.ddlDias.choices[0][0])]
    #[(dia.nro, dia.desc) for dia in dt.GetDiasDisponiblesxSacerdoteyCentro(sacerdote.idSacerdote,)]
    return render_template('turnoSacerdote.html', image_name = rutaImagen, sacerdote = sacerdote, form = form)

@app.route('/turnoCentro/<int:idCentro>')
def turnoCentro(idCentro):
    dc = DatosCentros()
    centro = dc.GetOne(idCentro)
    rutaImangen = centro.nombre.replace(" ", "") + ".png"
    centro.sacerdotesyDisponibilidad = dc.GetSacerdotesyHorarios(centro)

    dt = DatosTurnos()
    ds = DatosSacerdotes()
    form = Controles()
    form.ddlSacerdotes.choices = [(sacerdote.id, sacerdote.apellidoNombre) for sacerdote in ds.GetAllxCentro(centro.idCentro)]
    form.ddlDias.choices = [(dia[0], dia[1]) for dia in dt.GetDiasDisponiblesxSacerdoteyCentro(form.ddlSacerdotes.choices[0][0], idCentro)]
    form.ddlTurnos.choices = [(turno[0], turno[1]) for turno in dt.GetPeriodosDisponiblesxSacerdoteCentroyDia(form.ddlSacerdotes.choices[0][0], idCentro, form.ddlDias.choices[0][0])]
    return render_template('turnoCentro.html', image_name= rutaImangen, centro = centro, form=form)


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

@app.route('/diasxSacerdoteyCentro/<int:idSacerdote>/<int:idCentro>')
def getDiasxSacerdoteyCentro (idSacerdote, idCentro):
    dt = DatosTurnos()
    
    diasLista = dt.GetDiasxSacerdoteyCentro(idSacerdote, idCentro)
    diasListaDict = []
    for dia in diasLista:
        diaDict = {}
        diaDict['id']=dia[0]
        diaDict['desc']=dia[1]
        diasListaDict.append(diaDict)
    
    return jsonify({'dias': diasListaDict})

@app.route('/periodosDisponiblesxSacerdoteyCentroyDia/<int:idSacerdote>/<int:idCentro>/<dia>')
def periodosDisponibles(idSacerdote, idCentro, dia):
    diaFormat = datetime.strptime(dia, '%d-%m-%Y')
    dt = DatosTurnos()
    periodosLista = dt.GetPeriodosDisponiblesxSacerdoteCentroyDia(idSacerdote, idCentro, diaFormat)
    periodosListaDict = []
    for p in periodosLista:
        pDict = {}
        pDict['fechayHora']=p[0]
        pDict['desc']=p[1]
        periodosListaDict.append(pDict)

    return jsonify({'periodos': periodosListaDict})

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


@app.route('/enviarMailConfirmacion/<mailDestinatario>/<int:idCentro>/<int:idSacerdote>/<fechayHoraTurno>')
def enviarMail(mailDestinatario, idCentro, idSacerdote, fechayHoraTurno):
    dt = DatosTurnos()
    turno = Turno()
    turno.idCentro = idCentro
    turno.idSacerdote = idSacerdote
    turno.mail = mailDestinatario
    turno.fechayHoraTurno = datetime.strptime(fechayHoraTurno, '%d-%m-%Y %H:%M')
    fecha = datetime.strftime(turno.fechayHoraTurno.date(), '%d-%m-%Y')
    hora = turno.fechayHoraTurno.time()
    mail = turno.mail

    dc = DatosCentros()
    centro = dc.GetOne(turno.idCentro)

    ds = DatosSacerdotes()
    sacerdote = ds.GetOne(turno.idSacerdote)

    msg = Message('Confirmar turno de confesión', recipients=[mailDestinatario])
    msg.html =  render_template('emailConfirmacion.html', mail = mail, centro = centro, sacerdote = sacerdote, fecha= fecha, hora = hora)
    FlaskMailApp.send(msg)
    return 'Mail enviado'

# Esto tendria que ser cambiado para no manejar ids a la vista de la gente
@app.route('/confirmarTurno/<mailDestinatario>/<int:idCentro>/<int:idSacerdote>/<fechayHoraTurno>')
def confirmarTurno(mailDestinatario, idCentro, idSacerdote, fechayHoraTurno):
    turno = Turno()
    turno.idCentro = idCentro
    turno.idSacerdote = idSacerdote
    turno.mail = mailDestinatario
    turno.fechayHoraTurno = datetime.strptime(fechayHoraTurno, '%d-%m-%Y %H:%M')
    fecha = datetime.strftime(turno.fechayHoraTurno.date(), '%d-%m-%Y')
    hora = turno.fechayHoraTurno.time()
    dt = DatosTurnos()
    if ( dt.InsertFiltrado(turno)):
        dc = DatosCentros()
        centro = dc.GetOne(turno.idCentro)
        ds = DatosSacerdotes()
        sacerdote = ds.GetOne(turno.idSacerdote)
        return render_template('turnoConfirmado.html', centroNombre = centro.nombre, sacerdoteNombre = sacerdote.apellidoNombre, fecha = fecha, hora = hora )
    else:
        return render_template('turnoConfirmado.html', centroNombre = "", sacerdoteNombre = "", fecha="", hora="")

@app.route('/cancelarTurno')
def cancelarTurno():
    return render_template('cancelarTurno.html')


@app.route('/enviarMailCancelacion/<emailPenitente>')
def emailCancelacion(emailPenitente):
    dt = DatosTurnos()
    dc = DatosCentros()
    ds = DatosSacerdotes()
    turnos = dt.getAllFuturosxPenitetes(emailPenitente)
    if turnos != []:
        turnosDatos=[]
        for t in turnos:
            centro = dc.GetOne(t.idCentro)
            sacerdote = ds.GetOne(t.idSacerdote)
            turnosDatos.append((t.idTurno, centro.nombre, sacerdote.apellidoNombre, t.fechayHoraTurno.date(), t.fechayHoraTurno.time()))
        msg = Message('Cancelacion de turnos de confesión', recipients=[emailPenitente])
        msg.html =  render_template('emailCancelacion.html',turnosDatos = turnosDatos)
        FlaskMailApp.send(msg)
        return 'Mail enviado'
    return 'Mail no enviado'

@app.route('/eliminarTurno/<int:idTurno>')
def eliminarTurno(idTurno):
    dt = DatosTurnos()
    turno = dt.deleteOne(idTurno)
    if ( turno != False):
        fecha = datetime.strftime(turno.fechayHoraTurno.date(), '%d-%m-%Y')
        hora = turno.fechayHoraTurno.time()
        dc = DatosCentros()
        centro = dc.GetOne(turno.idCentro)
        ds = DatosSacerdotes()
        sacerdote = ds.GetOne(turno.idSacerdote)
        resultado = True
        return render_template('turnoCancelado.html', resultado = resultado, centro = centro.nombre,  sacerdoteNombre = sacerdote.apellidoNombre, fecha = fecha, hora = hora )
    else:
        resultado = False
        return render_template('turnoCancelado.html', resultado = resultado, centro = "",  sacerdoteNombre = "", fecha = "", hora = "" )
# @app.route('/cancelarTurno', methods=['POST'])
# def enviarTurnos():
#     flash('Se ha enviado un mail con sus turnos')
#     mail = request.form.get('mail')
#     pass
    
@app.route('/profile')
@login_required
def profile():
    dc = DatosCentros()
    dt = DatosTurnos()
    form = Controles()
    form.ddlCentros.choices = [(centro.idCentro, centro.nombre + " , " + centro.direccion) for centro in dc.GetAllxSacerdote(current_user.id)]
    form.ddlDias.choices = [(dia[0], dia[1]) for dia in dt.GetDiasxSacerdoteyCentro(current_user.id, form.ddlCentros.choices[0][0])]
    return render_template('profile.html', sacerdote=current_user, form=form)

@app.route('/turnosxCentroyDia/<int:idCentro>/<dia>')
def turnoxCentro(idCentro, dia):
    dt = DatosTurnos()
    diaFormat = datetime.strptime(dia, '%d-%m-%Y')
    turnos = dt.GetAllxCentroyDia(idCentro, diaFormat.date())
    turnosListaDict = []
    for t in turnos:
        tDict = {}
        tDict['fechayHora']= datetime.strftime(t.fechayHoraTurno, '%H:%M')
        tDict['mail']= t.mail
        turnosListaDict.append(tDict)
    return jsonify({'turnos': turnosListaDict})


if __name__ == '__main__':    
    app.run(debug=True)
