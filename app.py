from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

users = {}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = generate_password_hash(request.form['password'])

    if username in users:
        return "User already exists!"

    users[username] = password
    return redirect('/')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    password = request.form['password']

    if username in users and check_password_hash(users[username], password):
        session['user'] = username
        return render_template('dashboard.html', user=username)
    else:
        return "Invalid Credentials"

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']

    if "fake" in text.lower():
        result = "Fake News ❌"
    else:
        result = "Real News ✅"

    return render_template('dashboard.html', user=session['user'], result=result)

if __name__ == '__main__':
    app.run(debug=True)