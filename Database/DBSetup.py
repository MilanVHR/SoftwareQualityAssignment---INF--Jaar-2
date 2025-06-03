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
            Driving_License_Number CHAR(9) PRIMARY KEY NOT NULL,
            First_Name VARCHAR,
            Last_Name VARCHAR,
            Birthday DATE,
            Gender VARCHAR,
            Street_Name VARCHAR,
            House_Number INT,
            Zip_Code CHAR(6),
            City VARCHAR,
            Email_Address VARCHAR,
            Mobile_Phone VARCHAR
        )
    ''')

def SetupServiceEngineer(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Service_Engineers (
            Username VARCHAR PRIMARY KEY NOT NULL,
            Password VARCHAR,
            First_Name VARCHAR,
            Last_Name VARCHAR,
            Registration_date DATE
        )
    ''')

def SetupSystemAdministrator(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS System_Administrators (
            Username VARCHAR PRIMARY KEY NOT NULL,
            Password VARCHAR,
            First_Name VARCHAR,
            Last_Name VARCHAR,
            Registration_date DATE
        )
    ''')

def SetupLog(cursor:Cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Logs (
            Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Date DATE,
            Time VARCHAR,
            Username VARCHAR,
            Description_of_activity DATE,
            Additional_Information VARCHAR,
            Suspicious BOOLEAN
        )
    ''')