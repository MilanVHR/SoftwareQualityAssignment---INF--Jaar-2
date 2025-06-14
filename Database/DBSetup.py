from sqlite3 import Cursor

def SetupScooters(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Scooters (
            Serial_Number VARCHAR(17) PRIMARY KEY NOT NULL,
            Brand VARCHAR,
            Model VARCHAR,
            Top_Speed INT,
            Battery_Capacity INT,
            State_of_Charge INT,
            Target_Range_SoC VARCHAR,
            Location VARCHAR,
            Is_Out_Of_Service BOOL,
            Mileage INT,
            Last_Maintenance_Date DATE
        )
    ''')

def SetupTraveller(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Travellers (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName BLOB,
            LastName BLOB,
            Birthday BLOB,
            Gender BLOB,
            StreetName BLOB,
            HouseNumber BLOB,
            ZipCode BLOB,
            City BLOB,
            EmailAddress BLOB,
            MobilePhone BLOB,
            DrivingLicenseNumber BLOB UNIQUE
        )
    ''')

def SetupServiceEngineer(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Service_Engineers (
            Username BLOB PRIMARY KEY NOT NULL,  
            Password BLOB,                      
            First_Name BLOB,                    
            Last_Name BLOB,                     
            Registration_date DATE
        )
    ''')

def SetupSystemAdministrator(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS System_Administrators (
            Username BLOB PRIMARY KEY NOT NULL,  
            Password BLOB,                      
            First_Name BLOB,                    
            Last_Name BLOB,                     
            Registration_date DATE
        )
    ''')

def SetupLog(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Logs (
            Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Date BLOB,                         
            Time BLOB,                         
            Username BLOB,                     
            Description_of_activity BLOB,      
            Additional_Information BLOB,       
            Suspicious BOOLEAN
        )
    ''')