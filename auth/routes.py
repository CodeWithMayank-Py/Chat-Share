# Authentication routes
from flask import render_template, request, redirect, url_for, flash, session
from .forms import RegistrationForm, LoginForm
from .storage import users
from .utils import hash_password, verify_password
from flask import Flask

# Import the Flask application instance from the __init__.py file
from . import auth_app

# Define the route for the index page
@auth_app.route('/')
def index():
    return render_template('index.html')

# Define the route for the registration page
@auth_app.route('/register')
def register():
    return render_template('registration.html')
