from datetime import datetime
from Controllers.Validations import isSerialNumberValid
from Controllers.Logging import log
from Database.DBCheckUser import Roles
from Menus.Overlapping_Menu import add_scooter_menu, own_profile_submenu, scooter_submenu, service_engineer_submenu, traveller_submenu, show_logs_menu
from Model.Scooter import addScooterToDatabase, Scooter


def system_admin_menu(connection, username):
    while True:
        print("\n=== SYSTEM ADMIN MENU ===")
        print("1. Beheer eigen profiel")
        print("2. Beheer Service Engineers")
        print("3. Beheer Travellers")
        print("4. Beheer Scooters")
        print("5. Backup en Restore")
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
            backup_restore_submenu()
        if choice == "6":
            show_logs_menu()
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


def backup_restore_submenu():
    while True:
        print("\n--- Backup en Restore ---")
        print("1. Backup maken van systeem")
        print("2. Restore-code genereren voor System Admin")
        print("3. Restore-code intrekken")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            log("back up created", "system_admin")
            print("→  Backup maken")  # (nog te implementeren)
        elif choice == "2":
            log("restore code generated", "system_admin")
            print("→  Restore-code genereren")  # (nog te implementeren)
        elif choice == "3":
            log("restore code deleted", "system_admin")
            print("→  Restore-code intrekken")  # (nog te implementeren)
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")

