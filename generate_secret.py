import secrets
import string

def generate_secret_key(length=32):
    """Generate a secure secret key"""
    return secrets.token_hex(length)

def generate_strong_password(length=32):
    """Generate a strong password with letters, digits, and symbols"""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

if __name__ == "__main__":
    print("Secret Key (hex):", generate_secret_key())
    print("Strong Password:", generate_strong_password())
