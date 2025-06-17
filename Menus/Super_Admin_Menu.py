

from datetime import datetime, timezone
from Controllers.Logging import log


from Controllers.Validations import isPasswordValid, isUsernameValid
from Menus.Overlapping_Menu import scooter_submenu, service_engineer_submenu, traveller_submenu, show_logs_menu
from Menus.System_Admin_Menu import backup_restore_submenu
from Model.System_Administrator import System_Administrator, addSystemAdministratorToDatabase, deleteSystemAdministratorFromDatabase


def super_admin_menu(connection):
    while True:
        print("\n=== SUPER ADMIN MENU ===")
        print("1. Beheer System Administrators")
        print("2. Beheer Service Engineers")
        print("3. Beheer Travellers")
        print("4. Beheer Scooters")
        print("5. Backup en Restore")
        print("6. Bekijk Logs")
        print("0. Log uit")

        choice = input("Maak een keuze: ")
        if choice == "1":
            system_admin_submenu(connection)
        elif choice == "2":
            service_engineer_submenu()
        elif choice == "3":
            traveller_submenu()
        elif choice == "4":
            scooter_submenu()
        elif choice == "5":
            backup_restore_submenu()
        elif choice == "6":
            show_logs_menu()
        elif choice == "0":
            print("Je bent uitgelogd.\n")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")


def system_admin_submenu(connection):
    while True:
        print("\n--- Beheer System Administrators ---")
        print("1. Nieuwe System Admin toevoegen")
        print("2. Gegevens van System Admin wijzigen")
        print("3. System Admin verwijderen")
        print("4. Wachtwoord resetten")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")

        if choice == "1":
            add_system_admin(connection)
        elif choice == "2":
            update_system_admin()
        elif choice == "3":
            delete_system_admin(connection)
        elif choice == "4":
            reset_system_admin_password()
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")


def add_system_admin(connection):
    print("\n--- Nieuwe System Administrator toevoegen ---")
    while True:
        username = input("Gebruikersnaam (8-10 tekens): ")
        if (isUsernameValid(username)):
            break

    while True:
        password = input("Wachtwoord: ")
        if (isPasswordValid(password)):
            break
    first_name = input("Voornaam: ")
    last_name = input("Achternaam: ")
    log("New admin user is created", "super_admin", f"username: {username}")

    # validatie + encryptie + toevoegen aan database
    toAdd = System_Administrator(
        username,
        password,
        first_name,
        last_name,
        datetime.now(timezone.utc)
    )
    addSystemAdministratorToDatabase(connection, toAdd)


def delete_system_admin(connection):
    print("\n--- Verwijder System Administrator ---")
    username = input("Gebruikersnaam van de admin die je wilt verwijderen: ")
    confirm = input(f"Weet je zeker dat je '{username}' wilt verwijderen? (ja/nee): ")

    if confirm.lower() == "ja":
        log("system admin is deleted", "super_admin", f"username: {username}")
        #  uit database verwijderen
        deleteSystemAdministratorFromDatabase(connection, username)
        print(f"🗑️ '{username}' gemarkeerd voor verwijdering.")  # (nog te implementeren)
    else:
        print("Verwijdering geannuleerd.")


def update_system_admin():
    print("\n--- Wijzig System Administrator ---")
    username = input("Gebruikersnaam van de admin die je wilt wijzigen: ")

    print("1. Voornaam wijzigen")
    print("2. Achternaam wijzigen")
    print("3. Rol wijzigen (meestal niet nodig)")
    choice = input("Wat wil je wijzigen? ")

    log("System admin has been updated", "super_admin", f"username: {username}")
    #  gegevens ophalen, wijzigen in de database
    print(f"Wijziging voor '{username}' voorbereid.")  # (nog te implementeren)


def reset_system_admin_password():
    print("\n--- Reset wachtwoord System Admin ---")
    username = input("Gebruikersnaam van de admin: ")
    temp_password = "TempPass123!"  # Is nu hardcoded, kan willekeurig worden nog

    log("System admin password has been reset", "super_admin", f"username: {username}")

    #  password reset logica + e-mail of melding
    print(f"🔑 Tijdelijk wachtwoord voor '{username}' is '{temp_password}'.")  # (nog te implementeren)
