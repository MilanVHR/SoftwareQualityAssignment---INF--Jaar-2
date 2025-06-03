from datetime import date
from datetime import time
from sqlite3 import Connection, Cursor

class Log:
    Date: date
    Time: time
    Username: str
    Description_of_activity: str
    Additional_Information: str
    Suspicious: bool

    def __init__(self, Date: date, Time: time, Username: str, Description_of_activity: str, Additional_Information: str, Suspicious: bool):
        self.Date = Date
        self.Time = Time
        self.Username = Username
        self.Description_of_activity = Description_of_activity
        self.Additional_Information = Additional_Information
        self.Suspicious = Suspicious
    
def addLogToDatabase(connection:Connection, log:Log):
    connection.cursor().execute("""
        INSERT INTO Logs 
        (Date, Time, Username, Description_of_activity, Additional_Information, Suspicious)
        VALUES (?, ?, ?, ?, ?, ?)
    """, 
    (log.Date, f"{log.Time}", log.Username, 
    log.Description_of_activity, log.Additional_Information, log.Suspicious))
    connection.commit()

def deleteLogFromDatabase(connection:Connection ,Id: int):
    connection.cursor().execute("DELETE FROM Logs WHERE Id = ?", (Id,))
    connection.commit()