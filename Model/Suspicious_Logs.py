from datetime import datetime, timezone
from sqlite3 import Connection, Cursor

from Encryption.Encryptor import Decrypt, Encrypt

class Suspicious_Logs:
    Data: str

    def __init__(self, data:str):
        self.Data = data

def insertSusLog(connection: Connection, data:str):
    connection.cursor().execute("""
    INSERT INTO Suspicious_Logs (Data)
    VALUES (?)
    """, (data,))
    connection.commit()