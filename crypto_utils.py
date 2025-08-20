
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    with open(filepath, 'wb') as f:
        f.write(encrypted)

def decrypt_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    decrypted = cipher.decrypt(data)
    with open(filepath, 'wb') as f:
        f.write(decrypted)
