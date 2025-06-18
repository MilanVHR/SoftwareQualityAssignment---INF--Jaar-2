from datetime import datetime
import sqlite3
from Controllers.Logging import log, readLog, readSuspiciousLog
import time

from Database.DBCheckUser import Roles
from Encryption.Encryptor import Decrypt, Encrypt, Hash
from Model.Scooter import Scooter, addScooterToDatabase


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


def scooter_submenu(connection):
    while True:
        print("\n--- Beheer Scooters ---")
        print("1. Nieuwe scooter toevoegen")
        print("2. Scootergegevens wijzigen")
        print("3. Scooter verwijderen")
        print("4. Scooter zoeken")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            add_scooter_menu(connection)
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

def add_scooter_menu(connection):
    brand = input("Voer de brand van de scooter in:")
    model = input("Voer de model van de scooter in:")
    serial_number = "@@@"
    while not isSerialNumberValid(serial_number) or not serial_number.isalnum():
        serial_number = input("Voer 10-17 alfanumeriek tekens in van serial number in: ")
        if not isSerialNumberValid(serial_number):
            print("Serial number is te lang of te kort")
        if not serial_number.isalnum():
            print("Serial number bevat niet toegestaande karakters")

    top_speed_input = ""
    while not top_speed_input.isnumeric() or int(top_speed_input) < 0:
        top_speed_input = input("Voer de top speed van de scooter in, alleen nummer en grooter dan 0: ")
        if not top_speed_input.isnumeric():
            print("Gebruik alleen maar nummers")
        if top_speed_input.isnumeric() and int(top_speed_input) < 0:
            print("Top speed moet grooter dan")
    top_speed = int(top_speed_input)

    battery_capacity_input = ""
    while not battery_capacity_input.isnumeric() or int(battery_capacity_input) < 0:
        battery_capacity_input = input("Voer de batterijcapaciteit de scooter in, alleen nummer en grooter dan 0: ")
    battery_capacity = int(battery_capacity_input)

    soc_input = ""
    while not soc_input.isnumeric() or not (0 <= int(soc_input) <= 100):
        soc_input = input("Voer de State of Charge (0-100%) in: ")
    state_of_charge = int(soc_input)

    min_soc = -1
    max_soc = -2
    while max_soc < min_soc:
        min_soc_input = ""
        while not min_soc_input.isnumeric() or not (0 <= int(min_soc_input) <= 100):
            min_soc_input = input("Voer het minimale Target Range SoC in (0-100): ")
        min_soc = int(min_soc_input)

        max_soc_input = ""
        while not max_soc_input.isnumeric() or not (0 <= int(max_soc_input) <= 100) or int(max_soc_input) < min_soc:
            max_soc_input = input(f"Voer het maximale Target Range SoC in (tussen {min_soc} en 100): ")
        max_soc = int(max_soc_input)
        if max_soc < min_soc:
            print("het minimale target range is grooter dan maximale range")
    target_range_soc = f"min: {min_soc}%, max: {max_soc}"

    location_valid = False
    while not location_valid:
        try:
            lat = float(input("Voer de latitude in: "))
            lon = float(input("Voer de longitude in: "))
            location = (lat, lon)
            location_valid = True
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")

    valid_oos = False
    while not valid_oos:
        out_of_service_input = input("Is de scooter buiten gebruik? (ja/nee): ").strip().lower()
        if out_of_service_input in ("ja", "nee"):
            is_out_of_service = out_of_service_input == "ja"
            valid_oos = True
        else:
            print("Ongeldige invoer, typ 'ja' of 'nee'.")

    mileage_input = ""
    while not mileage_input.isnumeric() or int(mileage_input) < 0:
        mileage_input = input("Voer de kilometerstand in (alleen nummer): ")
    mileage = int(mileage_input)

    valid_date = False
    while not valid_date:
        date_input = input("Voer de laatste onderhoudsdatum in (DD-MM-YYYY): ")
        try:
            last_maintenance_date = datetime.strptime(date_input, "%d-%m-%Y").date()
            valid_date = True
        except ValueError:
            print("Ongeldige datum, probeer opnieuw.")

    toAdd = Scooter(
        serial_number,
        brand,
        model,
        top_speed,
        battery_capacity,
        state_of_charge,
        target_range_soc,
        location,
        is_out_of_service,
        mileage,
        last_maintenance_date)
    addScooterToDatabase(connection, toAdd)
    log("added new scooter", "system_admin", f"serial number: {serial_number}")

