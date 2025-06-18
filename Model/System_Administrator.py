from datetime import date
from sqlite3 import Connection

from Encryption.Encryptor import Decrypt, Encrypt, Hash

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
        (Encrypt(admin.Username), Hash(admin.Password), Encrypt(admin.First_Name), Encrypt(admin.Last_Name), f"{admin.Registration_date}"))
    connection.commit()

def deleteSystemAdministratorFromDatabase(connection:Connection ,Username: str):
    connection.cursor().execute("DELETE FROM System_Administrators WHERE Username = ?", (Encrypt(Username),))
    connection.commit()

def updateSystemAdministratorInDatabase(connection: Connection, admin: System_Administrator):
    connection.cursor().execute("""UPDATE System_Administrators
        SET Password = ?, First_Name = ?, Last_Name = ?, Registration_date = ?
        WHERE Username = ?""", 
        (admin.Password, Encrypt(admin.First_Name), Encrypt(admin.Last_Name), f"{admin.Registration_date}", Encrypt(admin.Username)))
    connection.commit()


def decryptSystemAdministrator(encrypted_data):
    return System_Administrator(
        Username=Decrypt(encrypted_data['Username']),
        Password=encrypted_data['Password'],
        First_Name=Decrypt(encrypted_data['First_Name']),
        Last_Name=Decrypt(encrypted_data['Last_Name']),
        Registration_date=encrypted_data['Registration_date']
    )


def findSystemAdministrator(cursor, Username=None, First_Name=None, Last_name=None, Registration_date=None):
    cursor.execute("SELECT * FROM System_Administrators")
    # Fetching all isnt a very good idea in production
    # however I have not foun a way to support partial
    # parameters and encrypted columns
    encrypted_rows = cursor.fetchall()
    SystemAdministrators = []

    for row in encrypted_rows:
        encrypted_data = {
            'Username': row[0],
            'Password': row[1],
            'First_Name': row[2],
            'Last_Name': row[3],
            'Registration_date': row[4]
        }

        # Use decryptSystemAdministrator to get a SystemAdministrator object
        SystemAdministrator = decryptSystemAdministrator(encrypted_data)

        # the " ... is not None check" just skips that parameter if it has not been provided in the function
        if (
        Username is not None and 
        str(Username).lower() not in str(SystemAdministrator.Username).lower()):
            continue
        if (
        First_Name is not None and 
        str(First_Name).lower() not in str(SystemAdministrator.First_Name).lower()):
            continue
        if (
        Last_name is not None and 
        str(Last_name).lower() not in str(SystemAdministrator.Last_Name).lower()):
            continue
        if (
        Registration_date is not None and 
        str(Registration_date) not in str(SystemAdministrator.Registration_date)):
            continue

        SystemAdministrators.append(SystemAdministrator)

    return SystemAdministrators