# Utility functions for authentication
from passlib.hash import bcrypt

# Function to hash a password
def hash_password(password):
    return bcrypt.hash(password)

# Functions to verify a password
def verify_password(password, hashed_password):
    return bcrypt.verify(password, hashed_password)