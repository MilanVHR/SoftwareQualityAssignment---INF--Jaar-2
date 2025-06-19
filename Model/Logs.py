from datetime import datetime, timezone
from sqlite3 import Connection, Cursor

from Encryption.Encryptor import Decrypt, Encrypt

class Logs:
    Data: str

    def __init__(self, data:str):
        self.Data = data

def insertLog(connection: Connection, data:str):
    connection.commit()

    connection.cursor().execute("""INSERT INTO Logs (Data)VALUES (?)""",
        (
            data,
        ))