import flask
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

from 

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=60)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sacerdotes')
def sacerdotes():
    return render_template('sacerdotes.html')

@app.route('/centros')
def centro():
    return render_template('centros.html')

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