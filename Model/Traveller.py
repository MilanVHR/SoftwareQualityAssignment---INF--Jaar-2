from datetime import date
from enum import Enum
from sqlite3 import Connection

class CityEnum(Enum):
    ROTTERDAM = "Rotterdam"
    AMSTERDAM = "Amsterdam"
    UTRECHT = "Utrecht"
    THE_HAGUE = "The Hague"
    EINDHOVEN = "Eindhoven"
    GRONINGEN = "Groningen"
    MAASTRICHT = "Maastricht"
    LEIDEN = "Leiden"
    DELFT = "Delft"
    BREDA = "Breda"

# D = (0-9)
# X = (A-Z)
class Traveller:
    # XXDDDDDDD or XDDDDDDDD
    Driving_License_Number: str
    First_Name: str
    Last_Name: str
    Birthday: date
    Gender: str
    Street_Name: str
    House_Number: int
    # DDDDXX
    Zip_Code: str
    # The system should generate a list of 10 predefined city names of your choice.
    City: CityEnum
    Email_Address: str
    # +31-6-DDDDDDDD Only DDDDDDDD to be entered by the user.
    Mobile_Phone: str
    

    def __init__(self, Driving_License_Number: str, First_Name: str, Last_Name: str, Birthday: date, Gender: str, Street_Name: str, House_Number: str, Zip_Code: str, City: CityEnum, Email_Address: str, Mobile_Phone: str):
        self.Driving_License_Number = Driving_License_Number
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Birthday = Birthday
        self.Gender = Gender
        self.Street_Name = Street_Name
        self.House_Number = House_Number
        self.Zip_Code = Zip_Code
        self.City = City
        self.Email_Address = Email_Address
        self.Mobile_Phone = Mobile_Phone
    
def addTravellerToDatabase(connection:Connection, traveller:Traveller):
    connection.cursor().execute(
        "INSERT INTO Travellers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (traveller.Driving_License_Number, traveller.First_Name, traveller.Last_Name, 
        f"{traveller.Birthday}", traveller.Gender, traveller.Street_Name, 
        traveller.House_Number, traveller.Zip_Code, traveller.City.value, 
        traveller.Email_Address, traveller.Mobile_Phone))
    connection.commit()

def deleteTravellerFromDatabase(connection:Connection ,license_number: str):
    connection.cursor().execute("DELETE FROM Travellers WHERE Driving_License_Number = ?", (license_number,))
    connection.commit()

def updateTravellerInDatabase(connection: Connection, traveller: Traveller):
    connection.cursor().execute("""UPDATE Travellers
        SET First_Name = ?, Last_Name = ?, Birthday = ?, Gender = ?, Street_Name = ?, House_Number = ?, Zip_Code = ?, City = ?, Email_Address = ?, Mobile_Phone = ?
        WHERE Driving_License_Number = ?""", 
        (traveller.First_Name, traveller.Last_Name, f"{traveller.Birthday}", traveller.Gender, traveller.Street_Name, traveller.House_Number, traveller.Zip_Code, traveller.City.value, traveller.Email_Address, traveller.Mobile_Phone, traveller.Driving_License_Number))
    connection.commit()
