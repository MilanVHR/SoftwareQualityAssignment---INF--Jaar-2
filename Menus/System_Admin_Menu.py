from datetime import datetime
from Controllers.Validations import isSerialNumberValid
from Controllers.Logging import checkIfUnreadSuspiciousLogs, log
from Database.DBBackUp import Backup_database, Restore_database
from Database.DBCheckUser import Roles
from Menus.Overlapping_Menu import add_scooter_menu, own_profile_submenu, scooter_submenu, service_engineer_submenu, traveller_submenu, show_logs_menu
from Model.Backup_Code import findBackupCode
from Model.Scooter import addScooterToDatabase, Scooter


def system_admin_menu(connection, username):
    while True:
        print("\n=== SYSTEM ADMIN MENU ===")
        print("1. Beheer eigen profiel")
        print("2. Beheer Service Engineers")
        print("3. Beheer Travellers")
        print("4. Beheer Scooters")
        print("5. Backup en Restore")
        if (checkIfUnreadSuspiciousLogs(connection, username)):
            print("6. Bekijk Logs ‼ ongelezen verdachte logs ‼")
        else:
            print("6. Bekijk Logs")
        print("0. Log uit")

        choice = input("Maak een keuze: ")
        if choice == "1":
            own_profile_submenu(connection, username, Roles.System_Admin)
        if choice == "2":
            service_engineer_submenu()
        if choice == "3":
            traveller_submenu()
        if choice == "4":
            scooter_submenu(connection)
        if choice == "5":
            backup_restore_submenu_System_Admin(connection, username)
        if choice == "6":
            show_logs_menu(connection, username)
        if choice == "0":
            print("Je bent uitgelogd.\n")
            break


def scooter_submenu(connection):
    while True:
        print("\n--- Beheer Scooters ---")
        print("1. Nieuwe scooter toevoegen")
        print("2. Scootergegevens wijzigen")
        print("3. Scooter verwijderen")
        print("4. Scooter zoeken")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            add_scooter_menu(connection)
        elif choice == "2":
            print("→  Wijzigen van een scooter")  # (nog te implementeren)
        elif choice == "3":
            print("→  Verwijderen van een scooter")  # (nog te implementeren)
        elif choice == "4":
            print("→  Zoekfunctie voor scooter")  # (nog te implementeren)
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")



def backup_restore_submenu_System_Admin(connection, username):
    while True:
        print("\n--- Backup en Restore ---")
        print("1. Backup maken van systeem")
        print("2. Restore-code gebruiken om te herstellen")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            createdPath = Backup_database()
            print(f"Back up is aangemaakt: {createdPath}")
            log(connection, "Created backup", username, f"backup filename: {createdPath}")
        elif choice == "2":
            backup_restore_menu(connection, username)
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")

def backup_restore_menu(connection, username):
    while True:
        print("\n--- Backup restoren ---")
        code = input("Voer de herstel code in:")
        
        foundBackupCodes = findBackupCode(connection.cursor(), code, username)
        if (len(foundBackupCodes) == 0):
            print(f"Geen bruikbare backups gevonden met code: {code}")
        elif (len(foundBackupCodes) > 0):
            print(f"Backup code gevonden met code:'{foundBackupCodes[0].Code}'. Is dit juist?")
            print("1. Ja, herstel deze backup")
            print("2. Nee")
            print("0. Menu verlaten")
            confirmation = input("Maak een keuze:")
            if (confirmation == "1"):
                log(connection, "backup code restored", username, f"using code: {foundBackupCodes[0].Code}, file: {foundBackupCodes[0].Filename}")
                Restore_database(foundBackupCodes[0].Filename)
                break
            elif (confirmation == "0"):
                return