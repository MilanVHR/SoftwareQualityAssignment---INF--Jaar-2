from datetime import datetime, timezone
from sqlite3 import Connection, Cursor

from Encryption.Encryptor import Decrypt, Encrypt

class last_Read_Log:
    Username: str
    Read_date: datetime

    def __init__(self, username:str, read_date:datetime):
        self.Username = username
        self.Read_date = read_date

# update or insert
def upsertLastReadLog(connection: Connection, username):
    sql = """
    INSERT INTO Last_Read_Log (Username, Read_date)
    VALUES (?, ?)
    ON CONFLICT(Username) DO UPDATE SET
        Read_date = excluded.Read_date
    """
    connection.cursor().execute(sql, (Encrypt(username), f"{datetime.now(timezone.utc)}"))
    connection.commit()

def findLastReadLog(cursor:Cursor, username:str) -> last_Read_Log:
    cursor.execute("SELECT * FROM Last_Read_Log")
    # Fetching all isnt a very good idea in production
    # however I have not foun a way to support partial
    # parameters and encrypted columns
    encrypted_rows = cursor.fetchall()

    for row in encrypted_rows:
        lastReadLog = last_Read_Log(
            Decrypt(row[0]),
            datetime.fromisoformat(row[1])
        )

        # the " ... is not None check" just skips that parameter if it has not been provided in the function
        if (lastReadLog.Username != username):
            continue

        return lastReadLog

    return None