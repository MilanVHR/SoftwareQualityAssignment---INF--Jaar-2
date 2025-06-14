def own_profile_submenu():  # (nog te implementeren)
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