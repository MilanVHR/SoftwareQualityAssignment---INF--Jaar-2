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
    login_menu()