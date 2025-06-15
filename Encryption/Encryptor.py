from cryptography.hazmat.primitives.ciphers.aead import AESSIV
from cryptography.hazmat.primitives import hashes

def Encrypt(object):
    key = b""
    with open("./Encryption/encryption_key.bin","rb",) as keyFile:
        key = keyFile.read()
    aes_siv = AESSIV(key)
    return aes_siv.encrypt(bytes(object.encode()), [b''])

def Decrypt(encrypted):
    key = b""
    with open("./Encryption/encryption_key.bin","rb",) as keyFile:
        key = keyFile.read()
    aes_siv = AESSIV(key)
    return str(aes_siv.decrypt(encrypted, [b''])).strip('b').strip("'")

def Hash(password):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(password.encode('utf-8'))
    return digest.finalize()