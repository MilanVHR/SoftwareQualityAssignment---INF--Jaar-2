from enum import Enum
from sqlite3 import Cursor

from Encryption.Encryptor import Encrypt, Hash

class Roles(Enum):
    System_Admin = "System_Admin"
    Service_Engineer = "Service_Engineer"

def check_service_engineer(cursor: Cursor, username, password):
    encrypted_username = Encrypt(username)
    hashed_password = Hash(password)

    found = cursor.execute("""
        SELECT * FROM Service_Engineers WHERE Username = ? AND Password = ?
    """, (encrypted_username, hashed_password)).fetchone()
    if found != None:
        return True
    else:
        return False

def check_system_admin(cursor: Cursor, username, password):
    encrypted_username = Encrypt(username)
    hashed_password = Hash(password)

    found = cursor.execute("""
        SELECT * FROM System_Administrators WHERE Username = ? AND Password = ?
    """, (encrypted_username, hashed_password)).fetchone()
    if found != None:
        return True
    else:
        return False

def check_role(cursor, username, password):
    if check_system_admin(cursor, username, password):
        return Roles.System_Admin
    
    if check_service_engineer(cursor, username, password):
        return Roles.Service_Engineer
    
    return None