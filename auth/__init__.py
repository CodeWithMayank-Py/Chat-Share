from flask import Flask

# Create the Flask application instance
auth_app = Flask(__name__, 
                 template_folder='C:\\Users\\paliw\\OneDrive\\Documents\\YT Playlist\\chat-share\\templates',
                   static_folder='C:\\Users\\paliw\\OneDrive\\Documents\\YT Playlist\\chat-share\\static')

# Import routes from the auth module
from . import routes
