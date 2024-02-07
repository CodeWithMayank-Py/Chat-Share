# Utility functions for authentication
from passlib.hash import pbkdf2_sha256
import secrets
from cryptography.fernet import Fernet
# Function to hash a password
def hash_password(password):
    return pbkdf2_sha256.hash(password)

# Functions to verify a password
def verify_password(password, hashed_password):
    return pbkdf2_sha256.verify(password, hashed_password)


# Functions to create secret key
def generate_secret_key():
    """
    Generate a random 32-byte secret key.
    Returns:
        str: The generated secret key as a hexadecimal string.
    """
    secret_key_bytes = secrets.token_bytes(32)
    return secret_key_bytes.hex()
