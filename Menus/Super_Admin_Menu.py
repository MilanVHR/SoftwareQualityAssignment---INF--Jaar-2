




from Menus.Overlapping_Menu import scooter_submenu, service_engineer_submenu, traveller_submenu
from Menus.System_Admin_Menu import backup_restore_submenu


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

def delete_system_admin():
    print("\n--- Verwijder System Administrator ---")
    username = input("Gebruikersnaam van de admin die je wilt verwijderen: ")
    confirm = input(f"Weet je zeker dat je '{username}' wilt verwijderen? (ja/nee): ")
    
    if confirm.lower() == "ja":
        #  uit database verwijderen
        print(f"🗑️ '{username}' gemarkeerd voor verwijdering.") # (nog te implementeren)
    else:
        print("Verwijdering geannuleerd.")

def update_system_admin():
    print("\n--- Wijzig System Administrator ---")
    username = input("Gebruikersnaam van de admin die je wilt wijzigen: ")
    
    print("1. Voornaam wijzigen")
    print("2. Achternaam wijzigen")
    print("3. Rol wijzigen (meestal niet nodig)")
    choice = input("Wat wil je wijzigen? ")

    #  gegevens ophalen, wijzigen in de database
    print(f"Wijziging voor '{username}' voorbereid.") # (nog te implementeren)

def reset_system_admin_password():
    print("\n--- Reset wachtwoord System Admin ---")
    username = input("Gebruikersnaam van de admin: ")
    temp_password = "TempPass123!"  # Is nu hardcoded, kan willekeurig worden nog
    
    #  password reset logica + e-mail of melding
    print(f"🔑 Tijdelijk wachtwoord voor '{username}' is '{temp_password}'.") # (nog te implementeren)
