from flask import Flask
import os
from .utils import generate_secret_key

# Get the absolute path of the current directory
current_dir = os.path.dirname(__file__)

# Define the paths relative to the current directory
template_folder = os.path.join(current_dir, 'templates')
static_folder = os.path.join(current_dir, 'static')

# Create the Flask application instance
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

# Set the secret key for session management
app.secret_key = generate_secret_key()

# Import routes from the auth module
from . import routes

# If needed, include the run logic directly for development:
if __name__ == "__main__":
    app.run(debug=True)         # Run the Flask app in debug mode
