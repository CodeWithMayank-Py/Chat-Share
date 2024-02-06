# Authentication routes
# Import neccessary modules
from flask import render_template, request, redirect, url_for, flash, session
from . import auth_app
from .forms import RegistrationForm, LoginForm
from .storage import users
from .utils import hash_password, verify_password
from flask import Flask


# Define the routes for the index page
@auth_app.route('/')
def index():
    return render_template('index.html')

@auth_app.route('/static/<path:path>')
def static_file(path):
    return auth_app.send_static_file(path)

# Route for user registration
@auth_app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('registration.html')

# Route for user login
@auth_app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = users.get(email)
    if user and verify_password(password, user['password']):
        # Store user identifier in session after successful login
        session['user_email'] = email
        flash('Login successful.', 'success')
        return redirect(url_for('chat_room'))
    else:
        flash('Invalid email or password. Please try again.', 'error')
        return redirect(url_for('login'))


if __name__ == '__main__':
    auth_app.run(debug=True)