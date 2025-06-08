from datetime import date
from sqlite3 import Connection

class Service_Engineer:
    Username: str
    Password: str
    First_Name: str
    Last_Name: str
    Registration_date: date

    def __init__(self, Username: str, Password: str, First_Name: str, Last_Name: str, Registration_date: date):
        self.Username = Username
        self.Password = Password
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Registration_date = Registration_date
    
def addServiceEngineerToDatabase(connection:Connection, engineer:Service_Engineer):
    connection.cursor().execute("""INSERT INTO Service_Engineers 
        (Username, Password, First_Name, Last_Name, Registration_date) 
        VALUES (?, ?, ?, ?, ?)""",
        (engineer.Username, engineer.Password, engineer.First_Name, engineer.Last_Name, f"{engineer.Registration_date}"))
    connection.commit()

def deleteServiceEngineerFromDatabase(connection:Connection ,Username: str):
    connection.cursor().execute("DELETE FROM Service_Engineers WHERE Username = ?", (Username,))
    connection.commit()

def updateServiceEngineerInDatabase(connection: Connection, engineer: Service_Engineer):
    connection.cursor().execute("""UPDATE Service_Engineers
        SET Password = ?, First_Name = ?, Last_Name = ?, Registration_date = ?
        WHERE Username = ?""", 
        (engineer.Password,engineer.First_Name,engineer.Last_Name,f"{engineer.Registration_date}",engineer.Username))
    connection.commit()