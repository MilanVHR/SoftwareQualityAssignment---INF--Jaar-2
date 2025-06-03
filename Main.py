import sqlite3
import Database.DBSetup as db

if __name__ == "__main__":
    connection = sqlite3.connect('SQAssignmentDB.db')
    cursor = connection.cursor()
    db.SetupScooters(cursor)
    db.SetupTraveller(cursor)
    db.SetupServiceEngineer(cursor)
    db.SetupSystemAdministrator(cursor)
    db.SetupLog(cursor)