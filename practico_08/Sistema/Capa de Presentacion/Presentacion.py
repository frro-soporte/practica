from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=60)

@app.route('/')
def home():
    return render_template('new.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user

        flash('Login succesful!')
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash('Alredy logged in!')
            return redirect(url_for('user'))
            
        return render_template('login.html')

@app.route('/user', methods=['POST','GET'])
def user():
    email = None    
    if 'user' in session: 
        user = session['user']

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            flash('Email was saved')
        else:
            if 'email' in session:
                email = session['email']

        return render_template('user.html', email = email)
    else:
        flash('You are not logged in')
        return redirect(url_for('login'))    

@app.route('/logout')
def logout(): 
    flash('You have been logged out', 'info')
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

# @app.route('/<usr>')
# def user(usr):
#     return f'<h1>{usr}</h1>'

# @app.route('/test')
# def test():
#     return render_template('new.html')

# @app.route('/admin')
# def admin():
#     return redirect(url_for('user', name='Administrador!'))

if __name__ == '__main__':
    app.run(debug=True)