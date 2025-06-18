from datetime import date
from sqlite3 import Connection

from Encryption.Encryptor import Decrypt, Encrypt, Hash

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

def findBackupCode(cursor, Code, systemAdminUsername=None):
    cursor.execute("SELECT * FROM Backup_Codes")
    # Fetching all isnt a very good idea in production
    # however I have not foun a way to support partial
    # parameters and encrypted columns
    encrypted_rows = cursor.fetchall()
    backupCodes = []

    for row in encrypted_rows:
        backupCode = Backup_Code(
            Decrypt(row[0]),
            Decrypt(row[1]),
            Decrypt(row[2])
        )

        # the " ... is not None check" just skips that parameter if it has not been provided in the function
        if (
        str(Code) not in str(backupCode.Code)):
            continue
        if (
        systemAdminUsername is not None and 
        str(systemAdminUsername).lower() not in str(backupCode.System_Administrator_Username).lower()):
            continue

        backupCodes.append(backupCode)

    return backupCodes