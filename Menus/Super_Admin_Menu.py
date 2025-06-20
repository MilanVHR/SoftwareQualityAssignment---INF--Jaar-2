

from datetime import date
import os
import random
import string
from Controllers.Logging import checkIfUnreadSuspiciousLogs, log


from Controllers.Validations import isPasswordValid, isUsernameValid
from Database.DBBackUp import Backup_database, Restore_database
from Encryption.Encryptor import Hash
from Menus.Overlapping_Menu import scooter_submenu, service_engineer_submenu, traveller_submenu, show_logs_menu
from Model.Backup_Code import addBackUpCodeToDatabase, Backup_Code, deleteBackUpCodeFromDatabase, findBackupCode
from Model.System_Administrator import System_Administrator, addSystemAdministratorToDatabase, deleteSystemAdministratorFromDatabase, findSystemAdministrator, updateSystemAdministratorInDatabase


def super_admin_menu(connection):
    while True:
        print("\n=== SUPER ADMIN MENU ===")
        print("1. Beheer System Administrators")
        print("2. Beheer Service Engineers")
        print("3. Beheer Travellers")
        print("4. Beheer Scooters")
        print("5. Backup en Restore")
        if (checkIfUnreadSuspiciousLogs(connection, "super_admin")):
            print("6. Bekijk Logs ‼ ongelezen verdachte logs ‼")
        else:
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
            backup_submenu(connection)
        elif choice == "6":
            show_logs_menu(connection, "super_admin")
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
        else:
            print("Gebruikersnaam moet tussen 8-10 tekens zitten")

    while True:
        print("Wachtwoord moet een lengte hebben van minimaal 12 tekens")
        print("Wachtwoord mag niet langer zijn dan 30 tekens")
        print("Wachtwoord mag letters (a-z), (A-Z), cijfers (0-9), speciale tekens zoals ~!@#$%&_-+=`|$$){}[]:;'<>,.?/ bevatten")
        print("Wachtwoord moet een combinatie bevatten van minstens één kleine letter, één hoofdletter, één cijfer en één speciaal teken")
        password = input("Wachtwoord: ")
        if (isPasswordValid(password)):
            break
    first_name = input("Voornaam: ")
    last_name = input("Achternaam: ")
    log(connection, "New admin user is created", "super_admin", f"username: {username}")

    # validatie + encryptie + toevoegen aan database
    toAdd = System_Administrator(
        username,
        password,
        first_name,
        last_name,
        date.today()
    )
    addSystemAdministratorToDatabase(connection, toAdd)
    print("Toegevoegd een nieuwe system administrator\n")


def delete_system_admin(connection):
    print("\n--- Verwijder System Administrator ---")
    username = input("Gebruikersnaam van de admin die je wilt verwijderen: ")
    confirm = input(f"Weet je zeker dat je '{username}' wilt verwijderen? (ja/nee): ")

    if confirm.lower() == "ja":
        log(connection, "system admin is deleted", "super_admin", f"username: {username}")
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
        else:
            print(f"Geen systeem admins gevonden met: {username}")
            print("Opnieuw zoeken?")
            print("1. Ja")
            print("2. Nee, menu verlaten")
            confirmation = input("Maak een keuze:")
            if (confirmation == "2"):
                return
    
    sysAdminToChange = system_administrators[0]
    while True:
        print("1. Voornaam wijzigen")
        print("2. Achternaam wijzigen")
        print("3. Wachtwoord wijzigen")
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
        elif (choice == "3"):
            while True:
                print("Wachtwoord moet een lengte hebben van minimaal 12 tekens")
                print("Wachtwoord mag niet langer zijn dan 30 tekens")
                print("Wachtwoord mag letters (a-z), (A-Z), cijfers (0-9), speciale tekens zoals ~!@#$%&_-+=`|$$){}[]:;'<>,.?/ bevatten")
                print("Wachtwoord moet een combinatie bevatten van minstens één kleine letter, één hoofdletter, één cijfer en één speciaal teken")
                newPassword = input("Wachtwoord: ")
                if (isPasswordValid(newPassword)):
                    break
            sysAdminToChange.Password = Hash(newPassword)
            break
            
        elif (choice == "0"):
            return
        
        
    updateSystemAdministratorInDatabase(connection, sysAdminToChange)
    log(connection, "System admin has been updated", "super_admin", f"username: {username}")
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
    

    log(connection, "System admin password has been reset", "super_admin", f"username: {username}")

    #  password reset logica + e-mail of melding
    print(f"🔑 Tijdelijk wachtwoord voor '{username}' is '{temp_password}'.")


def backup_submenu(connection):
    while True:
        print("\n--- Backup en Restore ---")
        print("1. Backup maken van systeem")
        print("2. Restore-code genereren voor System Admin")
        print("3. Restore-code intrekken")
        print("4. Backup gebruiken")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            createdPath = Backup_database()
            print(f"Back up is aangemaakt: {createdPath}")
            log(connection, "Created backup", "super_admin", f"backup filename: {createdPath}")
        elif choice == "2":
            backup_create_code_submenu(connection)
        elif choice == "3":
            backup_delete_code_submenu(connection)
        elif choice == "4":
            backup_restore_submenu(connection)
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")

def backup_create_code_submenu(connection):
    while True:
        print("\n--- Backup code genereren ---")
        backup_file_names = [f for f in os.listdir("./Backups/") if os.path.isfile(os.path.join("./Backups/", f))]
        for file in backup_file_names:
            print(file)
        print("0. Terug naar vorige menu")
        choice = input("Voer de naam in van de backup: ")

        if (choice == "0"):
            return
        
        if (choice in backup_file_names):
            break
    
    code = generate_random_code()

    while True:
        system_admin_username = input("Gebruikersnaam van de systeem admin die de code mag gebruiken: ")

        system_administrators = findSystemAdministrator(connection.cursor(), system_admin_username)
        if (len(system_administrators) > 0):
            print(f"System Administrator met de gebruikers naam: '{system_administrators[0].Username}' gevonden. Is dit juist?")
            print("1. Ja")
            print("2. Nee")
            print("0. Menu verlaten")
            confirmation = input("Maak een keuze:")
            if (confirmation == "1"):
                break
            elif (confirmation == "0"):
                return
        else:
            print(f"Geen systeem admins gevonden met: {system_admin_username}")
            print("Opnieuw zoeken?")
            print("1. Ja")
            print("2. Nee, menu verlaten")
            confirmation = input("Maak een keuze:")
            if (confirmation == "2"):
                return

    
    backupCode = Backup_Code(
        choice,
        code,
        system_administrators[0].Username
    )
    addBackUpCodeToDatabase(connection, backupCode)

    print(f"\nBackup code: '{code}' aangemaakt voor: '{system_administrators[0].Username}'")
    log(connection, "backup code created", "super_admin", f"for system admin: {system_administrators[0].Username}, filename: {choice}")

def generate_random_code(length=10):
    # Define the characters to use
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    # Generate the random code
    return ''.join(random.choice(characters) for _ in range(length))

def backup_delete_code_submenu(connection):
    while True:
        print("\n--- Verwijderen van een Backup Code ---")
        backupCode = input("Voer code in die verwijdert moet worden: ")

        backupCodes = findBackupCode(connection.cursor(), backupCode)
        if (len(backupCodes) > 0):
            print(f"Backup code gevonden met code:'{backupCodes[0].Code}' voor systeem admin:{backupCodes[0].System_Administrator_Username}. Is dit juist?")
            print("1. Ja, verwijder")
            print("2. Nee en behou")
            print("0. Menu verlaten")
            confirmation = input("Maak een keuze:")
            if (confirmation == "1"):
                break
            elif (confirmation == "0"):
                return
        else:
            print(f"Geen backup codes gevonden met code: {backupCode}")
            print("Opnieuw zoeken?")
            print("1. Ja")
            print("2. Nee, menu verlaten")
            confirmation = input("Maak een keuze:")
            if (confirmation == "2"):
                return
    
    deleteBackUpCodeFromDatabase(connection, backupCodes[0].Code)
    print(f"backup code: {backupCodes[0].Code} verwijdert")
    log(connection, "backup code created", "super_admin", f"for system admin: {backupCodes[0].System_Administrator_Username}, filename: {backupCodes[0].Filename}")


def backup_restore_submenu(connection):
    while True:
        print("\n--- Backup herstellen ---")
        backup_file_names = [f for f in os.listdir("./Backups/") if os.path.isfile(os.path.join("./Backups/", f))]
        for file in backup_file_names:
            print(file)
        print("0. Terug naar vorige menu")
        choice = input("Voer de naam in van de backup: ")

        if (choice == "0"):
            return
        
        if (choice in backup_file_names):
            break

    while True:
        confirmation = input(f"Weet je zeker dat je backup '{choice}' wilt herstellen? (ja/nee):)")
        if (confirmation.lower() == "ja"):
            break
        elif (confirmation.lower() == "nee"):
            return
    Restore_database(choice)
    log(connection, "backup code restored", "super_admin", f"filename: {choice}")

