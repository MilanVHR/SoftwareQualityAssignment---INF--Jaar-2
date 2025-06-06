import sqlite3
import Database.DBSetup as db
import pwinput

def super_admin_menu():
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
            system_admin_submenu()
        elif choice == "2":
            service_engineer_submenu()
        elif choice == "3":
            traveller_submenu()
        elif choice == "4":
            scooter_submenu()
        elif choice == "5":
            backup_restore_submenu()
        elif choice == "6":
            print("→ Logs bekijken (nog te implementeren)")
        elif choice == "0":
            print("Je bent uitgelogd.")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
        

def system_admin_menu():
    while True:
        print("\n=== SYSTEM ADMIN MENU ===")
        print("1. Beheer eigen profiel")
        print("2. Beheer Service Engineers")
        print("3. Beheer Travellers")
        print("4. Beheer Scooters")
        print("5. Backup / Restore")
        print("6. Bekijk Logs")
        print("0. Log uit")

        choice = input("Maak een keuze: ")
        if choice == "1":
            break
        if choice == "2":
            break
        if choice == "3":
            break
        if choice == "4":
            break
        if choice == "5":
            break
        if choice == "6":
            break
        if choice == "0":
            break
        

def service_engineer_menu():
    while True:
        print("\n=== SERVICE ENGINEER MENU ===")
        print("1. Update wachtwoord")
        print("2. Bekijk/Update scooters")
        print("3. Zoek scooters")
        print("0. Log uit")

        choice = input("Maak een keuze: ")
        if choice == "1":
            break
        if choice == "2":
            break
        if choice == "3":
            break
        if choice == "0":
            break
        # Voeg hier acties toe

def system_admin_submenu():
    while True:
        print("\n--- Beheer System Administrators ---")
        print("1. Nieuwe System Admin toevoegen")
        print("2. Gegevens van System Admin wijzigen")
        print("3. System Admin verwijderen")
        print("4. Wachtwoord resetten")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            print("→ Toevoegen van een System Admin ") # (nog te implementeren)
        elif choice == "2":
            print("→ Wijzigen van een System Admin ") # (nog te implementeren)
        elif choice == "3":
            print("→ Verwijderen van een System Admin ") # (nog te implementeren)
        elif choice == "4":
            print("→ Reset wachtwoord voor een System Admin ") # (nog te implementeren)
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")


def service_engineer_submenu():
    while True:
        print("\n--- Beheer Service Engineers ---")
        print("1. Nieuwe Service Engineer toevoegen")
        print("2. Gegevens van Service Engineer wijzigen")
        print("3. Service Engineer verwijderen")
        print("4. Wachtwoord resetten")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            print("→ Toevoegen van een Service Engineer") # (nog te implementeren) 
        elif choice == "2":
            print("→  Wijzigen van een Service Engineer") # (nog te implementeren)
        elif choice == "3":
            print("→  Verwijderen van een Service Engineer") # (nog te implementeren)
        elif choice == "4":
            print("→  Reset wachtwoord voor een Service Engineer") # (nog te implementeren)
        elif choice == "0":
            break
        else:
            print("❌ Ongeldige keuze.")


def traveller_submenu():
    while True:
        print("\n--- Beheer Travellers ---")
        print("1. Nieuwe Traveller toevoegen")
        print("2. Travellergegevens wijzigen")
        print("3. Traveller verwijderen")
        print("4. Traveller zoeken")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            print("→  Toevoegen van een Traveller") # (nog te implementeren)
        elif choice == "2":
            print("→  Wijzigen van een Traveller") # (nog te implementeren)
        elif choice == "3":
            print("→  Verwijderen van een Traveller") # (nog te implementeren)
        elif choice == "4":
            print("→  Zoekfunctie voor Traveller") # (nog te implementeren)
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")


def scooter_submenu():
    while True:
        print("\n--- Beheer Scooters ---")
        print("1. Nieuwe scooter toevoegen")
        print("2. Scootergegevens wijzigen")
        print("3. Scooter verwijderen")
        print("4. Scooter zoeken")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            print("→  Toevoegen van een scooter") # (nog te implementeren)
        elif choice == "2":
            print("→  Wijzigen van een scooter") # (nog te implementeren)
        elif choice == "3":
            print("→  Verwijderen van een scooter") # (nog te implementeren)
        elif choice == "4":
            print("→  Zoekfunctie voor scooter") # (nog te implementeren)
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
            print("→  Backup maken") # (nog te implementeren)
        elif choice == "2":
            print("→  Restore-code genereren") # (nog te implementeren)
        elif choice == "3":
            print("→  Restore-code intrekken") # (nog te implementeren)
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")



def login_menu():
    print("=== URBAN MOBILITY BACKEND SYSTEM ===")
    print("Log in als een gebruiker\n")

    username = input("Gebruikersnaam: ")
    password = pwinput.pwinput(prompt='Wachtwoord: ', mask='*')

    # TIJDELIJKk: hardcoded superadmin
    if username == "super_admin" and password == "Admin_123?":
        super_admin_menu()
    else:
        # Checken in de databasse
        print("Onjuiste inloggegevens of nog niet geïmplementeerd.")
        # system_admin_menu() en service_engineer_menu() aanroepen

if __name__ == "__main__":
    connection = sqlite3.connect('SQAssignmentDB.db')
    cursor = connection.cursor()
    db.SetupScooters(cursor)
    db.SetupTraveller(cursor)
    db.SetupServiceEngineer(cursor)
    db.SetupSystemAdministrator(cursor)
    db.SetupLog(cursor)
    login_menu()
