from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sys
sys.path.append('C:/Users/arias/Desktop/UTN/SGDPV/frro-soporte-2020-23/practico_08/Sistema/Capa de Datos')
from Clases import Sacerdote
from Metodos import DatosSacerdotes
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html')    

@auth.route('/login', methods=['POST'])
def login_post():
    mail = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    ds = DatosSacerdotes()
    sacerdote = ds.GetOneMail(mail)

    if not sacerdote and not check_password_hash(sacerdote.password, password):
        flash('Revisa el mail y la contraseña')       
        return redirect(url_for('auth.login'))    
    
    # Crea la cookie y la sesion para este sacerdote
    login_user(sacerdote, remember=remember) 

    return redirect(url_for('profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')
    
@auth.route('/signup', methods=['POST'])
def signup_post():
    mail = request.form.get('email')
    apellidoNombre = request.form.get('name')
    password = request.form.get('password')

    ds = DatosSacerdotes()
    sacerdote = ds.GetOneMail(mail)

    if sacerdote:
        flash('El mail ya se encuentra registrado')
        return redirect(url_for('auth.signup'))
    
    nuevo_sacerdote = Sacerdote()
    nuevo_sacerdote.apellidoNombre = apellidoNombre
    nuevo_sacerdote.mail = mail    
    nuevo_sacerdote.password = generate_password_hash(password, method='sha256')

    ds.Add(nuevo_sacerdote)

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
 
