import sqlite3
from Controllers.Logging import readLog, readSuspiciousLog
import time

from Database.DBCheckUser import Roles
from Encryption.Encryptor import Decrypt, Encrypt, Hash


def own_profile_submenu(connection, username, role):
    while True:
        print("\n--- Beheer Eigen Profiel ---")
        print("1. Bekijk profiel")
        print("2. Wijzig voornaam of achternaam")
        print("3. Wijzig wachtwoord")
        print("4. Verwijder mijn account")
        print("0. Terug")

        choice = input("Maak een keuze: ")

        if choice == "1":
            view_own_profile(connection.cursor(), username, role)
        elif choice == "2":
            update_own_name(connection, username, role)
        elif choice == "3":
            change_own_password(connection, username, role)
        elif choice == "4":
            delete_own_account(connection, username, role)
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
            # (nog te implementeren)
            print("→ Toevoegen van een Service Engineer")
        elif choice == "2":
            # (nog te implementeren)
            print("→  Wijzigen van een Service Engineer")
        elif choice == "3":
            # (nog te implementeren)
            print("→  Verwijderen van een Service Engineer")
        elif choice == "4":
            # (nog te implementeren)
            print("→  Reset wachtwoord voor een Service Engineer")
        elif choice == "0":
            break
        else:
            print("Ongeldige keuze.")


def traveller_submenu(connection):
    while True:
        print("\n--- Beheer Travellers ---")
        print("1. Nieuwe Traveller toevoegen")
        print("2. Travellergegevens wijzigen")
        print("3. Traveller verwijderen")
        print("4. Traveller zoeken")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            add_traveller(connection)
        elif choice == "2":
            update_traveller(connection)
        elif choice == "3":
            delete_traveller(connection)
        elif choice == "4":
            find_traveller(connection)
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


def view_own_profile(cursor, username, role):
    if role == Roles.Service_Engineer:
        cursor.execute("SELECT * FROM Service_Engineers WHERE username=?",
                       (Encrypt(username),))
    else:
        cursor.execute("SELECT * FROM System_Administrators WHERE username=?",
                       (Encrypt(username),))
    result = cursor.fetchone()

    if result:
        print("\n👤 Profielgegevens:")
        print(f"Voornaam: {Decrypt(result[2])}")
        print(f"Achternaam: {Decrypt(result[3])}")
        print(f"Geregistreerd op: {result[4]}")
    else:
        print("Profiel niet gevonden.")


def update_own_name(connection, username, role):
    first = input("Nieuwe voornaam (Enter om te behouden): ")
    last = input("Nieuwe achternaam (Enter om te behouden): ")
    cursor = connection.cursor()

    if role == Roles.Service_Engineer:
        if first:
            cursor.execute("UPDATE Service_Engineers SET First_Name=? WHERE Username=?",
                           (Encrypt(first), Encrypt(username)))
        if last:
            cursor.execute("UPDATE Service_Engineers SET Last_Name=? WHERE Username=?",
                           (Encrypt(last), Encrypt(username)))
    else:
        if first:
            cursor.execute("UPDATE System_Administrators SET First_Name=? WHERE Username=?",
                           (Encrypt(first), Encrypt(username)))
        if last:
            cursor.execute("UPDATE System_Administrators SET Last_Name=? WHERE Username=?",
                           (Encrypt(last), Encrypt(username)))

    connection.commit()
    print("Naam bijgewerkt.")


def change_own_password(connection, username, role):
    newPassword = input("Nieuwe wachtwoord (Enter om te behouden): ")
    cursor = connection.cursor()
    if role == Roles.Service_Engineer:
        if newPassword:
            cursor.execute("UPDATE Service_Engineers SET Password=? WHERE Username=?",
                           (Hash(newPassword), Encrypt(username)))
        else:
            if newPassword:
                cursor.execute("UPDATE System_Administrators SET Password=? WHERE Username=?",
                               (Hash(newPassword), Encrypt(username)))


def delete_own_account(connection, username, role):
    confirm = input(
        f"Weet je zeker dat je jouw account '{username}' wilt verwijderen? (ja/nee): ")
    if confirm.lower() == "ja":
        cursor = connection.cursor()

        if role == Roles.Service_Engineer:
            cursor.execute("DELETE FROM Service_Engineers WHERE username=?",
                           (Encrypt(username),))
        else:
            cursor.execute("DELETE FROM System_Administrators WHERE username=?",
                           (Encrypt(username),))

        connection.commit()

        print(" Account verwijderd. Je bent nu uitgelogd.")
        time.sleep(3)
        exit()  # Verlaat de applicatie na verwijderen
    else:
        print("Verwijdering geannuleerd.")


def show_logs():
    while True:
        print("\n--- Reguliere logs ---")
        logs = readLog()

        for log in logs:
            print(log)

        print("0. Terug naar menu")
        choice = input("Maak een keuze: ")
        if choice == "0":
            break


def show_suspicious_logs():
    while True:
        print("\n--- Verdachte logs ---")
        logs = readSuspiciousLog()

        for log in logs:
            print(log)

        print("0. Terug naar menu")
        choice = input("Maak een keuze: ")
        if choice == "0":
            break


def show_logs_menu():
    while True:
        print("\n--- Bekijk logs ---")
        print("1. Bekijk de reguliere logs")
        print("2. Bekijk de verdachte logs")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            show_logs()
        elif choice == "2":
            show_suspicious_logs()
        elif choice == "0":
            break


def add_traveller(connection):
    print("\n--- Nieuwe Traveller toevoegen ---")
    first = input("Voornaam: ")
    last = input("Achternaam: ")
    birthday = input("Geboortedatum (YYYY-MM-DD): ")
    gender = input("Geslacht: ")
    street = input("Straatnaam: ")
    number = input("Huisnummer: ")
    zip_code = input("Postcode: ")
    city = input("Woonplaats: ")
    email = input("E-mailadres: ")
    phone = input("Mobiel nummer: ")
    license = input("Rijbewijsnummer: ")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Travellers WHERE EmailAddress = ?", (email,))
    if cursor.fetchone():
        print("Een traveller met dit e-mailadres bestaat al.")
        return

    cursor.execute("""
        INSERT INTO Travellers 
        (FirstName, LastName, Birthday, Gender, StreetName, HouseNumber, ZipCode, City, EmailAddress, MobilePhone, DrivingLicenseNumber)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (first, last, birthday, gender, street, number, zip_code, city, email, phone, license))
    connection.commit()
    print("Traveller succesvol toegevoegd.")
