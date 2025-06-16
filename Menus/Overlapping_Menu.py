import sqlite3


def own_profile_submenu():
    while True:
        print("\n--- Beheer Eigen Profiel ---")
        print("1. Bekijk profiel")
        print("2. Wijzig voornaam of achternaam")
        print("3. Wijzig wachtwoord")
        print("4. Verwijder mijn account")
        print("0. Terug")

        choice = input("Maak een keuze: ")

        if choice == "1":
            view_own_profile()
        elif choice == "2":
            update_own_name()
        elif choice == "3":
            change_own_password()
        elif choice == "4":
            delete_own_account()
        elif choice == "0":
            break


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
            print("→ Toevoegen van een Service Engineer")  # (nog te implementeren)
        elif choice == "2":
            print("→  Wijzigen van een Service Engineer")  # (nog te implementeren)
        elif choice == "3":
            print("→  Verwijderen van een Service Engineer")  # (nog te implementeren)
        elif choice == "4":
            print("→  Reset wachtwoord voor een Service Engineer")  # (nog te implementeren)
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
            print("→  Toevoegen van een Traveller")  # (nog te implementeren)
        elif choice == "2":
            print("→  Wijzigen van een Traveller")  # (nog te implementeren)
        elif choice == "3":
            print("→  Verwijderen van een Traveller")  # (nog te implementeren)
        elif choice == "4":
            print("→  Zoekfunctie voor Traveller")  # (nog te implementeren)
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
            print("→  Toevoegen van een scooter")  # (nog te implementeren)
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


def view_own_profile(user):
    conn = sqlite3.connect("urban_mobility.db")
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, registration_date FROM users WHERE LOWER(username)=?",
                   (user["username"].lower(),))
    result = cursor.fetchone()
    conn.close()

    if result:
        print("\n👤 Profielgegevens:")
        print(f"Voornaam: {result[0]}")
        print(f"Achternaam: {result[1]}")
        print(f"Geregistreerd op: {result[2]}")
    else:
        print("Profiel niet gevonden.")


def update_own_name(user):
    first = input("Nieuwe voornaam (Enter om te behouden): ")
    last = input("Nieuwe achternaam (Enter om te behouden): ")

    conn = sqlite3.connect("urban_mobility.db")
    cursor = conn.cursor()

    if first:
        cursor.execute("UPDATE users SET first_name=? WHERE LOWER(username)=?", (first, user["username"].lower()))
    if last:
        cursor.execute("UPDATE users SET last_name=? WHERE LOWER(username)=?", (last, user["username"].lower()))

    conn.commit()
    conn.close()
    print("Naam bijgewerkt.")


def change_own_password(user):
    return


def delete_own_account(user):
    confirm = input(f"Weet je zeker dat je jouw account '{user['username']}' wilt verwijderen? (ja/nee): ")
    if confirm.lower() == "ja":
        conn = sqlite3.connect("urban_mobility.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE LOWER(username)=?", (user["username"].lower(),))
        conn.commit()
        conn.close()
        print(" Account verwijderd. Je bent nu uitgelogd.")
        exit()  # Verlaat de applicatie na verwijderen
    else:
        print("Verwijdering geannuleerd.")
