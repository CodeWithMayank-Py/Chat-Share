from flask import Flask
import os
from .utils import generate_secret_key

# Create the Flask application instance
app = Flask(__name__, 
                 template_folder='C:\\Users\\paliw\\Documents\\YT Playlist\\chat-share\\app\\templates', 
                 static_folder='C:\\Users\\paliw\\Documents\\YT Playlist\\chat-share\\static')

# Set the secret key for session management
app.secret_key = generate_secret_key()

# Import routes from the auth module
from . import routes

# If needed, include the run logic directly for development:
if __name__ == "__main__":
    app.run(debug=True)         # Run the Flask app in debug mode
