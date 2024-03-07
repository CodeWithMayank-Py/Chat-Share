from flask import Flask, render_template, request, redirect, url_for, flash
import json, secrets
from passlib.hash import pbkdf2_sha256

# Functions to create secret key
def generate_secret_key():
    """
    Generate a random 32-byte secret key.
    Returns:
        str: The generated secret key as a hexadecimal string.
    """
    secret_key_bytes = secrets.token_bytes(32)
    return secret_key_bytes.hex()

# Function to hash a password
def hash_password(password):
    return pbkdf2_sha256.hash(password)

# Functions to verify a password
def verify_password(password, hashed_password):
    return pbkdf2_sha256.verify(password, hashed_password)



app = Flask(__name__)
app.secret_key = generate_secret_key()

# Path to the JSON file
json_file = '/tmp/users.json'

# Define the route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the registration page
@app.route('/register')
def register():
    return render_template('registration.html')

# Define the route for the dashboard page
@app.route('/dashboard')
def chat_room():
    # Your view logic here
    return render_template('dashboard.html')


# Function to load user data from JSON file
def load_users():
    try:
        with open(json_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Function to save user data to JSON file
def save_users(users_data):
    with open(json_file, 'w') as f:
        json.dump(users_data, f, indent=4)


# Route for handling user registration
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Load existing user data from JSON file
        users_data = load_users()

        # Check if the email already exists in the user data
        if email in users_data:
            flash('Email already exists. Please choose another email.', 'error')
            return redirect(url_for('register'))  # Redirect to the signup page

        # Hash the password before storing
        hashed_password = hash_password(password)

        # Add new user data to the dictionary
        users_data[email] = {'name': name, 'password': hashed_password}

        # Save updated user data to JSON file
        save_users(users_data)

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('chat_room'))  # Redirect to the dashboard page after successful registration

    # Render the signup page template (if the request method is not POST)
    return render_template('registration.html')

# Route for handling user sign-in
@app.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Load existing user data from JSON file
        users_data = load_users()

        # Check if the email exists in the user data
        if email in users_data:
            # Verify the password
            stored_password = users_data[email]['password']
            if verify_password(password, stored_password):
                flash('Login successful.', 'success')
                return redirect(url_for('chat_room'))  # Redirect to the dashboard page
            else:
                flash('Invalid email or password. Please try again.', 'error')
        else:
            flash('User does not exist. Please sign up.', 'error')

    # Render the signin page template (if the request method is not POST or authentication fails)
    return redirect(url_for('register'))


if __name__ == '__main__':
    app.run(debug=True) 
