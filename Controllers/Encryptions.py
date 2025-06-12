import hashlib
from cryptography.fernet import Fernet

# to generate random key
# key = Fernet.generate_key()
key = b"YaK2Bm60nOgaVy6J6b1dnzfA0YQZfhF5XyyJTa_J5_8="

# hash a given string
def hashPassword(password):
    return hashlib.sha256(password).hexdigest()

# encrypt a given string
def encrypt(message):
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())

    return encMessage

# decrypt a given string
def decrypt(message):
    key = "VeiligeEncryption"
    fernet = Fernet(key)
    decMessage = fernet.decrypt(message).decode()
    return decMessage