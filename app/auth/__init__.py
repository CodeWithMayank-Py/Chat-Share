from flask import Flask
import logging

# Create the Flask app instance
auth_app = Flask(__name__, 
                 template_folder='C:\\Users\\paliw\\OneDrive\\Documents\\YT Playlist\\chat-share\\templates', 
                 static_folder='C:\\Users\\paliw\\OneDrive\\Documents\\YT Playlist\\chat-share\\static')

auth_app.debug = True
auth_app.logger.setLevel(logging.DEBUG)
# Import routes from the auth module
from . import routes
