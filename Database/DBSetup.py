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

def SetupBackupCodes(cursor: Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Backup_Codes (
            Filename VARCHAR NOT NULL,
            Code BLOB PRIMARY KEY NOT NULL,
            System_Administrator_Username BLOB,
            FOREIGN KEY(System_Administrator_Username) REFERENCES System_Administrators(Username)
        )
    ''')

def SetupLastReadSuspiciousLogs(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Last_Read_Log (
            Username BLOB PRIMARY KEY NOT NULL,
            Read_date DATE
        )
    ''')

def SetupLogs(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Logs (
            Data BLOB
        )
    ''')

def SetupSuspiciousLogs(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Suspicious_Logs (
            Data BLOB
        )
    ''')