from datetime import date, datetime
from enum import Enum
from sqlite3 import Connection

from Encryption.Encryptor import Decrypt, Encrypt

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
    encryptedData = encryptTraveller(traveller)
    connection.cursor().execute(""" INSERT INTO Travellers (
            FirstName, LastName, Birthday, Gender, StreetName, HouseNumber, 
            ZipCode, City, EmailAddress, MobilePhone, DrivingLicenseNumber
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            encryptedData['First_Name'],
            encryptedData['Last_Name'],
            encryptedData['Birthday'],
            encryptedData['Gender'],
            encryptedData['Street_Name'],
            encryptedData['House_Number'],
            encryptedData['Zip_Code'],
            encryptedData['City'],
            encryptedData['Email_Address'],
            encryptedData['Mobile_Phone'],
            encryptedData['Driving_License_Number'],
        ))
    connection.commit()

def deleteTravellerFromDatabase(connection:Connection ,license_number: str):
    connection.cursor().execute("DELETE FROM Travellers WHERE DrivingLicenseNumber = ?", (Encrypt(license_number),))
    connection.commit()

def updateTravellerInDatabase(connection: Connection, traveller: Traveller):
    encryptedData = encryptTraveller(traveller)
    connection.cursor().execute("""UPDATE Travellers
        SET FirstName = ?, LastName = ?, Birthday = ?, Gender = ?, StreetName = ?, HouseNumber = ?, ZipCode = ?, City = ?, EmailAddress = ?, MobilePhone = ?
        WHERE DrivingLicenseNumber = ?""", 
        (
            encryptedData['First_Name'],
            encryptedData['Last_Name'],
            encryptedData['Birthday'],
            encryptedData['Gender'],
            encryptedData['Street_Name'],
            encryptedData['House_Number'],
            encryptedData['Zip_Code'],
            encryptedData['City'],
            encryptedData['Email_Address'],
            encryptedData['Mobile_Phone'],
            encryptedData['Driving_License_Number']
        ))
    connection.commit()

def encryptTraveller(traveller: Traveller):
    encrypted_data = {}
    
    # Encrypt each field by converting to string, encoding to bytes, then encrypting
    encrypted_data['Driving_License_Number'] = Encrypt(traveller.Driving_License_Number)
    encrypted_data['First_Name'] = Encrypt(traveller.First_Name)
    encrypted_data['Last_Name'] = Encrypt(traveller.Last_Name)
    encrypted_data['Birthday'] = Encrypt(str(traveller.Birthday))
    encrypted_data['Gender'] = Encrypt(traveller.Gender)
    encrypted_data['Street_Name'] = Encrypt(traveller.Street_Name)
    encrypted_data['House_Number'] = Encrypt(str(traveller.House_Number))
    encrypted_data['Zip_Code'] = Encrypt(traveller.Zip_Code)
    encrypted_data['City'] = Encrypt(traveller.City.value)
    encrypted_data['Email_Address'] = Encrypt(traveller.Email_Address)
    encrypted_data['Mobile_Phone'] = Encrypt(traveller.Mobile_Phone)
    
    return encrypted_data

def decryptTraveller(encrypted_data):
    return Traveller(
        Driving_License_Number=Decrypt(encrypted_data['Driving_License_Number']),
        First_Name=Decrypt(encrypted_data['First_Name']),
        Last_Name=Decrypt(encrypted_data['Last_Name']),
        Birthday=Decrypt(encrypted_data['Birthday']),
        Gender=Decrypt(encrypted_data['Gender']),
        Street_Name=Decrypt(encrypted_data['Street_Name']),
        House_Number=Decrypt(encrypted_data['House_Number']),
        Zip_Code=Decrypt(encrypted_data['Zip_Code']),
        City=CityEnum(Decrypt(encrypted_data['City'])),
        Email_Address=Decrypt(encrypted_data['Email_Address']),
        Mobile_Phone=Decrypt(encrypted_data['Mobile_Phone'])
    )

def findTravellers(cursor, Driving_License_Number=None, First_Name=None, Last_Name=None, Birthday=None, Gender=None, Street_Name=None, House_Number=None, Zip_Code=None, City=None, Email_Address=None, Mobile_Phone=None
) -> list[Traveller]:
    cursor.execute("SELECT * FROM Travellers")
    # Fetching all isnt a very good idea in production
    # however I have not foun a way to support partial
    # parameters and encrypted columns
    encrypted_rows = cursor.fetchall()
    travellers = []

    for row in encrypted_rows:
        encrypted_data = {
            'First_Name': row[1],
            'Last_Name': row[2],
            'Birthday': row[3],
            'Gender': row[4],
            'Street_Name': row[5],
            'House_Number': row[6],
            'Zip_Code': row[7],
            'City': row[8],
            'Email_Address': row[9],
            'Mobile_Phone': row[10],
            'Driving_License_Number': row[11],
        }

        # Use decryptTraveller to get a Traveller object
        traveller = decryptTraveller(encrypted_data)

        # the " ... is not None check" just skips that parameter if it has not been provided in the function
        if (
        Driving_License_Number is not None and 
        str(Driving_License_Number).lower() not in str(traveller.Driving_License_Number).lower()):
            continue
        if (
        First_Name is not None and 
        str(First_Name).lower() not in str(traveller.First_Name).lower()):
            continue
        if (
        Last_Name is not None and 
        str(Last_Name).lower() not in str(traveller.Last_Name).lower()):
            continue
        if (
        Birthday is not None and 
        str(Birthday) not in str(traveller.Birthday)):
            continue
        if (
        Gender is not None and 
        str(Gender).lower() not in str(traveller.Gender).lower()):
            continue
        if (
        Street_Name is not None and 
        str(Street_Name).lower() not in str(traveller.Street_Name).lower()):
            continue
        if (
        House_Number is not None and 
        str(House_Number) not in str(traveller.House_Number)):
            continue
        if (
        Zip_Code is not None and 
        str(Zip_Code).lower() not in str(traveller.Zip_Code).lower()):
            continue
        if (
        City is not None and 
        str(City).lower() not in str(traveller.City).lower()):
            continue
        if (
        Email_Address is not None and 
        str(Email_Address).lower() not in str(traveller.Email_Address).lower()):
            continue
        if (
        Mobile_Phone is not None and 
        str(Mobile_Phone).lower() not in str(traveller.Mobile_Phone).lower()):
            continue

        travellers.append(traveller)

    return travellers

def printTravellersList(travellers: list[Traveller]):
    for i, traveller in enumerate(travellers, start=1):
        print(f"{i}. Namen: {traveller.First_Name} {traveller.Last_Name}, Geboortedatum: {traveller.Birthday}, Adres: {traveller.Street_Name} {traveller.House_Number}, {traveller.Zip_Code} {traveller.City.value}, Rijbewijsnummer: {traveller.Driving_License_Number}, Email: {traveller.Email_Address}, Mobiel: {traveller.Mobile_Phone}")
