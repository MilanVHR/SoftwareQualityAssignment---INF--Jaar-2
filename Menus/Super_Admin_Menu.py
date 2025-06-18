

from datetime import date
from Controllers.Logging import log


from Controllers.Validations import isPasswordValid, isUsernameValid
from Menus.Overlapping_Menu import scooter_submenu, service_engineer_submenu, traveller_submenu, show_logs_menu
from Model.System_Administrator import System_Administrator, addSystemAdministratorToDatabase, deleteSystemAdministratorFromDatabase, findSystemAdministrator, updateSystemAdministratorInDatabase


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
            service_engineer_submenu(connection)
        elif choice == "3":
            traveller_submenu(connection)
        elif choice == "4":
            scooter_submenu(connection)
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
            update_system_admin(connection)
        elif choice == "3":
            delete_system_admin(connection)
        elif choice == "4":
            reset_system_admin_password(connection)
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
        print("must have a length of at least 12 characters")
        print("must be no longer than 30 characters")
        print("can contain letters (a-z), (A-Z), numbers (0-9), Special characters such as ~!@#$%&_-+=`|\(){}[]:;'<>,.?/")
        print("must have a combination of at least one lowercase letter, one uppercase letter, one digit, and one special character")
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
        date.today()
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
        print(f"🗑️ '{username}' gemarkeerd voor verwijdering.")
    else:
        print("Verwijdering geannuleerd.")


def update_system_admin(connection):
    while True:
        print("\n--- Wijzig System Administrator ---")
        username = input("Gebruikersnaam van de admin die je wilt wijzigen: ")

        system_administrators = findSystemAdministrator(connection.cursor(), username)
        if (len(system_administrators) > 0):
            print(f"System Administrator met de gebruikers naam: '{system_administrators[0].Username}' gevonden. Is dit juist?")
            print("1. Ja")
            print("2. Nee")
            print("0. Menu verlaten")
            choice = input("Maak een keuze:")
            if (choice == "1"):
                break
            elif (choice == "0"):
                return
    
    sysAdminToChange = system_administrators[0]
    while True:
        print("1. Voornaam wijzigen")
        print("2. Achternaam wijzigen")
        print("0. Menu verlaten")
        choice = input("Wat wil je wijzigen? ")

        if (choice == "1"):
            newFirstName = input("Vul nieuwe voornaam in: ")
            sysAdminToChange.First_Name = newFirstName
            break
        elif (choice == "2"):
            newLastName = input("Vul nieuwe achternaam in: ")
            sysAdminToChange.Last_Name = newLastName
            break
        elif (choice == "0"):
            return
        
        
    updateSystemAdministratorInDatabase(connection, sysAdminToChange)
    log("System admin has been updated", "super_admin", f"username: {username}")
    #  gegevens ophalen, wijzigen in de database
    print(f"Wijziging voor '{username}' gemaakt.")


def reset_system_admin_password(connection):
    while True:
        print("\n--- Reset wachtwoord System Admin ---")
        username = input("Gebruikersnaam van de admin: ")

        system_administrators = findSystemAdministrator(connection.cursor(), username)
        if (len(system_administrators) > 0):
            print(f"System Administrator met de gebruikers naam: '{system_administrators[0].Username}' gevonden. Is dit juist?")
            print("1. Ja")
            print("2. Nee")
            print("0. Menu verlaten")
            choice = input("Maak een keuze:")
            if (choice == "1"):
                break
            elif (choice == "0"):
                return

    temp_password = "TempPass123!"  # Is nu hardcoded, kan willekeurig worden nog

    sysAdminToChange = system_administrators[0]
    sysAdminToChange.Password = hash(temp_password)

    updateSystemAdministratorInDatabase(connection, sysAdminToChange)
    

    log("System admin password has been reset", "super_admin", f"username: {username}")

    #  password reset logica + e-mail of melding
    print(f"🔑 Tijdelijk wachtwoord voor '{username}' is '{temp_password}'.")


def backup_restore_submenu():
    while True:
        print("\n--- Backup en Restore ---")
        print("1. Backup maken van systeem")
        print("2. Restore-code genereren voor System Admin")
        print("3. Restore-code intrekken")
        print("4. Backup gebruiken")
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
        elif choice == "4":
            log("Backup gebruikt", "system_admin")
            print("+  Backup is benut") # (nog te implementeren)
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")