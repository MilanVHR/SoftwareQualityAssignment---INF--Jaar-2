from datetime import date
import sqlite3
from Database.DBCheckUser import Roles, check_role
import Database.DBSetup as db
import getpass
import sys
import time
from Controllers.Logging import log

from Menus.Service_Engineer_Menu import service_engineer_menu
from Menus.Super_Admin_Menu import super_admin_menu
from Menus.System_Admin_Menu import system_admin_menu
from Model.Service_Engineer import Service_Engineer, addServiceEngineerToDatabase
from Model.System_Administrator import System_Administrator, addSystemAdministratorToDatabase


def login_menu(connection):
    attempts = 0
    while True:
        print("=== URBAN MOBILITY BACKEND SYSTEM ===")
        print("Log in als een gebruiker\n")

        username = input("Gebruikersnaam: ")
        password = getpass.getpass("Wachtwoord: ")

        role = check_role(cursor, username, password)

        # TIJDELIJKk: hardcoded superadmin
        if username == "super_admin" and password == "Admin_123?":
            log("logged in", username)
            super_admin_menu(connection)
        elif role == Roles.System_Admin:
            log("logged in", username)
            system_admin_menu(connection, username)  # TIJDELIJK
        elif role == Roles.Service_Engineer:
            log("logged in", username)
            service_engineer_menu(connection, username)  # TIJDELIJK
        else:
            # Checken in de databasse
            attempts += 1
            if (attempts == 3):
                log("Too many login attempts", "",
                    f"username: {username} is used for a login attempt with a wrong password", True)
                print("Teveel inlog pogingen.")
                login_timeout()
                attempts = 0
            else:
                log("Unsuccessful login", "",
                    f"username: {username} is used for a login attempt with a wrong password", True)
                print("Onjuiste inloggegevens.")
            # system_admin_menu() en service_engineer_menu() aanroepen


def login_timeout():
    # time out is 5 minutes
    total_seconds = 5 * 60
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
    db.SetupBackupCodes(cursor)
    # se = Service_Engineer(Username="Milan", Password="Uilskuiken69", First_Name="Milan", Last_Name="Versluis", Registration_date= date(2020, 12, 24))
    # sa = System_Administrator(Username="Esmée", Password="Uilskuiken69", First_Name="Esmée", Last_Name="Biersteker", Registration_date= date(2020, 12, 24))
    # addServiceEngineerToDatabase(connection, se)
    # addSystemAdministratorToDatabase(connection, se)
    login_menu(connection)
