from datetime import date

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