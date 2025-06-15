import sqlite3
import Database.DBSetup as db
import pwinput
import sys
import time
from Controllers.Logging import log

from Menus.Service_Engineer_Menu import service_engineer_menu
from Menus.Super_Admin_Menu import super_admin_menu
from Menus.System_Admin_Menu import system_admin_menu




def login_menu():
    attempts = 0
    while True:
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
            system_admin_menu() #TIJDELIJK
        elif username == "service_engineer" and password == "Service_123?":
            log("logged in", username)
            service_engineer_menu() #TIJDELIJK
        else:
            # Checken in de databasse
            attempts += 1
            if (attempts == 3):
                log("Too many login attempts", additional=f"username: \"{username}\" is used for a login attempt with a wrong password", critical=True)
                print("Teveel inlog pogingen.")
                login_timeout()
                attempts = 0
            else:
                log("Unsuccessful login", additional=f"username: \"{username}\" is used for a login attempt with a wrong password", critical=True)
                print("Onjuiste inloggegevens of nog niet geïmplementeerd.")
            # system_admin_menu() en service_engineer_menu() aanroepen

def login_timeout():
    total_seconds = 30
    try:
        for remaining_seconds in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining_seconds, 60)
            time_left = f"{mins:02}:{secs:02}"
            sys.stdout.write(f"\rU moet nog {time_left} minuten wachten")
            sys.stdout.flush()
            time.sleep(1)
        print("\n")
    # if user tries to escape timeout reset it
    except KeyboardInterrupt:
        login_timeout()

if __name__ == "__main__":
    connection = sqlite3.connect('SQAssignmentDB.db')
    cursor = connection.cursor()
    db.SetupScooters(cursor)
    db.SetupTraveller(cursor)
    db.SetupServiceEngineer(cursor)
    db.SetupSystemAdministrator(cursor)
    login_menu()
