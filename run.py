# run.py

from app import auth_app as app


if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
