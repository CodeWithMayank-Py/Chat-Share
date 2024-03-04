from flask import Flask
from .utils import generate_secret_key

# Create the Flask application instance
auth_app = Flask(__name__, 
                 template_folder='C:\\Users\\paliw\\Documents\\YT Playlist\\chat-share\\templates',
                   static_folder='C:\\Users\\paliw\\Documents\\YT Playlist\\chat-share\\static')

# Set the secret key for session management
auth_app.secret_key = generate_secret_key()
# Import routes from the auth module
from . import routes
