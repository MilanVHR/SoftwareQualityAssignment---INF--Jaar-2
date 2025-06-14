import sqlite3
import Database.DBSetup as db
import pwinput
from Controllers.Logging import log

from Menus.Super_Admin_Menu import super_admin_menu
from Menus.System_Admin_Menu import system_admin_menu




def login_menu():
    print("=== URBAN MOBILITY BACKEND SYSTEM ===")
    print("Log in als een gebruiker\n")

    username = input("Gebruikersnaam: ")
    password = pwinput.pwinput(prompt='Wachtwoord: ', mask='*')

    # TIJDELIJKk: hardcoded superadmin
    if username == "super_admin" and password == "Admin_123?":
        log("logged in", username)
        super_admin_menu()
    elif username == "system_admin" and password == "System_123?":
        log("logged in", username)
        system_admin_menu()
    else:
        # Checken in de databasse
        log("Unsuccessful login", additional=f"username: \"{username}\" is used for a login attempt with a wrong password", critical=True)
        print("Onjuiste inloggegevens of nog niet geïmplementeerd.")
        # system_admin_menu() en service_engineer_menu() aanroepen

if __name__ == "__main__":
    connection = sqlite3.connect('SQAssignmentDB.db')
    cursor = connection.cursor()
    db.SetupScooters(cursor)
    db.SetupTraveller(cursor)
    db.SetupServiceEngineer(cursor)
    db.SetupSystemAdministrator(cursor)
    login_menu()
