# run.py

from app.auth import auth_app


if __name__ == "__main__":
    auth_app.run(debug=True)  # Run the Flask app in debug mode
