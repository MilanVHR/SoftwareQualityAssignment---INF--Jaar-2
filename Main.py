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
        print("5. Backup en Restore")
        print("6. Bekijk Logs")
        print("0. Log uit")

        choice = input("Maak een keuze: ")
        if choice == "1":
            break
        if choice == "2":
            service_engineer_submenu()
        if choice == "3":
            traveller_submenu()
        if choice == "4":
            scooter_submenu()
        if choice == "5":
            backup_restore_submenu()
        if choice == "6":
            print("→ Logs bekijken (nog te implementeren)")
        if choice == "0":
            print("Je bent uitgelogd.")
            break
        

def service_engineer_menu(current_user):
    while True:
        print("\n=== SERVICE ENGINEER MENU ===")
        print("1. Beheer eigen profiel")
        print("2. Update scootergegevens (alleen toegestaan velden)")
        print("3. Zoek en bekijk scooterinformatie")
        print("0. Log uit")

        choice = input("Maak een keuze: ")

        if choice == "1":
            own_profile_menu(current_user) # (nog te implementeren)
        elif choice == "2":
            update_scooter_attributes(current_user)
        elif choice == "3":
            search_scooter()
        elif choice == "0":
            print("Je bent uitgelogd.")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")


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
            print("Ongeldige keuze.")


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
            add_system_admin()
        elif choice == "2":
            update_system_admin()
        elif choice == "3":
            delete_system_admin()
        elif choice == "4":
            reset_system_admin_password()
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")


def add_system_admin():
    print("\n--- Nieuwe System Administrator toevoegen ---")
    username = input("Gebruikersnaam (8-10 tekens): ")
    password = input("Wachtwoord: ")
    first_name = input("Voornaam: ")
    last_name = input("Achternaam: ")

    # validatie + encryptie + toevoegen aan database
    print(f"Nieuwe system admin '{username}' voorbereid voor toevoegen.") # (nog te implementeren)

def update_system_admin():
    print("\n--- Wijzig System Administrator ---")
    username = input("Gebruikersnaam van de admin die je wilt wijzigen: ")
    
    print("1. Voornaam wijzigen")
    print("2. Achternaam wijzigen")
    print("3. Rol wijzigen (meestal niet nodig)")
    choice = input("Wat wil je wijzigen? ")

    #  gegevens ophalen, wijzigen in de database
    print(f"Wijziging voor '{username}' voorbereid.") # (nog te implementeren)

def delete_system_admin():
    print("\n--- Verwijder System Administrator ---")
    username = input("Gebruikersnaam van de admin die je wilt verwijderen: ")
    confirm = input(f"Weet je zeker dat je '{username}' wilt verwijderen? (ja/nee): ")
    
    if confirm.lower() == "ja":
        #  uit database verwijderen
        print(f"🗑️ '{username}' gemarkeerd voor verwijdering.") # (nog te implementeren)
    else:
        print("Verwijdering geannuleerd.")

def reset_system_admin_password():
    print("\n--- Reset wachtwoord System Admin ---")
    username = input("Gebruikersnaam van de admin: ")
    temp_password = "TempPass123!"  # Is nu hardcoded, kan willekeurig worden nog
    
    #  password reset logica + e-mail of melding
    print(f"🔑 Tijdelijk wachtwoord voor '{username}' is '{temp_password}'.") # (nog te implementeren)


def own_profile_submenu(current_user): # (nog te implementeren)
    while True:
        print("\n--- Beheer Eigen Profiel ---")
        print("1. Bekijk profiel")
        print("2. Wijzig voornaam of achternaam")
        print("3. Wijzig wachtwoord")
        print("4. Verwijder mijn account")
        print("0. Terug")

        choice = input("Maak een keuze: ")

        if choice == "1":
            break
        elif choice == "2":
            break
        elif choice == "3":
            break
        elif choice == "4":
            break
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")


def update_scooter_attributes(user):
    print("\n--- Scootergegevens bijwerken (alleen toegestane velden) ---")
    scooter_id = input("Voer het ID of serienummer van de scooter in: ")

    #  Zoek scooter in DB en laat zien
    print("1. State of Charge (SoC) wijzigen")
    print("2. Locatie wijzigen (GPS-coördinaten)")
    print("3. Out-of-Service status wijzigen")
    print("4. Kilometerstand bijwerken")
    print("5. Laatste onderhoudsdatum bijwerken")
    print("0. Terug")

    choice = input("Welke eigenschap wil je bijwerken? ")

    if choice == "1":
        new_soc = input("Nieuwe SoC (%): ") # (nog te implementeren)
        #  DB-update
        print(f"SoC bijgewerkt naar {new_soc}%")
    elif choice == "2":
        lat = input("Nieuwe latitude (bijv. 51.9225): ") # (nog te implementeren)
        lon = input("Nieuwe longitude (bijv. 4.47917): ")
        #  DB-update
        print(f"Locatie bijgewerkt naar lat={lat}, lon={lon}")
    elif choice == "3":
        status = input("Is de scooter out-of-service? (ja/nee): ")# (nog te implementeren)
        #  DB-update
        print(f"Out-of-service status ingesteld op {status}")
    elif choice == "4":
        km = input("Nieuwe kilometerstand: ")# (nog te implementeren)
        #  DB-update
        print(f"Kilometerstand bijgewerkt naar {km} km")
    elif choice == "5":
        date = input("Nieuwe onderhoudsdatum (YYYY-MM-DD): ") # (nog te implementeren)
        #  DB-update
        print(f"Laatste onderhoudsdatum bijgewerkt naar {date}")
    elif choice == "0":
        return
    else:
        print("Ongeldige keuze.")


def search_scooter(): # (nog te implementeren)
    return


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
