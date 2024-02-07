from flask import Flask

# Create the Flask application instance
auth_app = Flask(__name__, template_folder='templates', static_folder='static')

# Import routes from the auth module
from auth import routes