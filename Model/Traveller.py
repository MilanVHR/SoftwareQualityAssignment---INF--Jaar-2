from datetime import date
from enum import Enum
# D = (0-9)
# X = (A-Z)
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
    
class Traveller:
    First_Name: str
    Last_Name: str
    Birthday: date
    Gender: str
    Street_Name: str
    House_Number: str
    # DDDDXX
    Zip_Code: str
    # The system should generate a list of 10 predefined city names of your choice.
    City: CityEnum
    Email_Address: str
    # +31-6-DDDDDDDD Only DDDDDDDD to be entered by the user.
    Mobile_Phone: str
    # XXDDDDDDD or XDDDDDDDD
    Driving_License_Number: str

    def __init__(self, First_Name: str, Last_Name: str, Birthday: date, Gender: str, Street_Name: str, House_Number: str, Zip_Code: str, City: str, Email_Address: str, Mobile_Phone: str, Driving_License_Number: str):
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
        self.Driving_License_Number = Driving_License_Number

