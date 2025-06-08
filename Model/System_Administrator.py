from datetime import date
from sqlite3 import Connection

class System_Administrator:
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

def addSystemAdministratorToDatabase(connection:Connection, admin:System_Administrator):
    connection.cursor().execute("""INSERT INTO System_Administrators 
        (Username, Password, First_Name, Last_Name, Registration_date) 
        VALUES (?, ?, ?, ?, ?)""",
        (admin.Username, admin.Password, admin.First_Name, admin.Last_Name, f"{admin.Registration_date}"))
    connection.commit()

def deleteSystemAdministratorFromDatabase(connection:Connection ,Username: str):
    connection.cursor().execute("DELETE FROM System_Administrators WHERE Username = ?", (Username,))
    connection.commit()

def updateSystemAdministratorInDatabase(connection: Connection, admin: System_Administrator):
    connection.cursor().execute("""UPDATE System_Administrators
        SET Password = ?, First_Name = ?, Last_Name = ?, Registration_date = ?
        WHERE Username = ?""", 
        (admin.Password, admin.First_Name, admin.Last_Name, f"{admin.Registration_date}", admin.Username))
    connection.commit()