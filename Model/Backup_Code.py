from datetime import date
from sqlite3 import Connection

from Encryption.Encryptor import Encrypt, Hash

class Backup_Code:
    Filename: str
    Code: str
    System_Administrator_Username: str

    def __init__(self, Filename: str, Code: str, System_Administrator_Username: str):
        self.Filename = Filename
        self.Code = Code
        self.System_Administrator_Username = System_Administrator_Username
    
def addBackUpCodeToDatabase(connection:Connection, BackupCode:Backup_Code):
    connection.cursor().execute("""INSERT INTO Backup_Codes 
        (Filename, Code, System_Administrator_Username) 
        VALUES (?, ?, ?)""",
        (Encrypt(BackupCode.Filename), Encrypt(BackupCode.Code), Encrypt(BackupCode.System_Administrator_Username) ))
    connection.commit()

def deleteBackUpCodeFromDatabase(connection:Connection ,Code: str):
    connection.cursor().execute("DELETE FROM Backup_Codes WHERE Code = ?", (Encrypt(Code),))
    connection.commit()