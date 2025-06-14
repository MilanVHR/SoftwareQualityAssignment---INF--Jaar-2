from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes

def Encrypt(object):
    key = b""
    with open("./Encryption/encryption_key.txt","r",) as keyFile:
        key = bytes(str(keyFile.readline()).encode())
    encryptor = Fernet(key)
    return encryptor.encrypt(bytes(str(object).encode("utf-8")))

def Decrypt(encrypted):
    key = b""
    with open("./Encryption/encryption_key.txt","r",) as keyFile:
        key = bytes(str(keyFile.readline()).encode())
    encryptor = Fernet(key)
    return str(encryptor.decrypt(encrypted)).strip('b').strip("'")

def Hash(password):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(password.encode('utf-8'))
    return digest.finalize()