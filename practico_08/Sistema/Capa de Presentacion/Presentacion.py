from flask import Flask, redirect, url_for, render_template, request, session
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
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session: 
        user = session['user']
        return f'<h1>{user}</h1>'
    else:
        return redirect(url_for('login'))    

@app.route('/logout')
def logout():
    session.pop('user', None)
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