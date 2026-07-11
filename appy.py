# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Temporary validation (replace with real one later)
        if username == 'admin' and password == '1234':
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials, try again!"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
