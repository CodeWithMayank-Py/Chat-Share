# Authentication routes
from flask import render_template, request, redirect, url_for, flash
from .forms import RegistrationForm
from .storage import users
from .utils import hash_password, verify_password

# Import the Flask application instance from the __init__.py file
from . import auth_app

# Define the route for the index page
@auth_app.route('/')
def index():
    return render_template('index.html')

# Route for rendering the registration page and handling form submissions
@auth_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and request.form['form_type'] == 'signup':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if the email already exists in the user storage
        if email in users:
            flash('Email already exists. Please choose another email.', 'error')
            return redirect(url_for('signup'))

        # Hash the password before storing
        hashed_password = hash_password(password)

        # Store the user information in the user storage
        users[email] = {'name': name, 'email': email, 'password': hashed_password}

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('register'))

    # Render the registration page template
    return render_template('registration.html')
