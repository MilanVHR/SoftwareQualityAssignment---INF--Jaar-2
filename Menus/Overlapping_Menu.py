from datetime import date
from datetime import datetime
import re
import sqlite3
from Controllers.Logging import checkIfUnreadSuspiciousLogs, log, readLog, readSuspiciousLog
import time

from Controllers.Validations import isEmailValid, isPasswordValid, isPhoneNumberValid, isSerialNumberValid, isZipcodeValid, isDriversLicenseValid
from Database.DBCheckUser import Roles
from Encryption.Encryptor import Decrypt, Encrypt, Hash
from Model.Scooter import Scooter, addScooterToDatabase, findScooters, printScootersList, updateScooterInDatabase
from Model.Traveller import CityEnum, Traveller, addTravellerToDatabase, deleteTravellerFromDatabase, findTravellers, printTravellersList, updateTravellerInDatabase


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


def service_engineer_submenu(connection):
    while True:
        print("\n--- Beheer Service Engineers ---")
        print("1. Nieuwe Service Engineer toevoegen")
        print("2. Gegevens van Service Engineer wijzigen")
        print("3. Service Engineer verwijderen")
        print("4. Wachtwoord resetten")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            add_service_engineer(connection)
        elif choice == "2":
            update_service_engineer(connection)
        elif choice == "3":
            delete_service_engineer(connection)
        elif choice == "4":
            reset_service_engineer_password(connection)
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
            update_scooter_menu(connection)
        elif choice == "3":
            delete_scooter_menu(connection)
        elif choice == "4":
            find_scooter_menu(connection)
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
        print("\nProfielgegevens:")
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
    while True:
        print("Wachtwoord moet een lengte hebben van minimaal 12 tekens")
        print("Wachtwoord mag niet langer zijn dan 30 tekens")
        print("Wachtwoord mag letters (a-z), (A-Z), cijfers (0-9), speciale tekens zoals ~!@#$%&_-+=`|$$){}[]:;'<>,.?/ bevatten")
        print("Wachtwoord moet een combinatie bevatten van minstens één kleine letter, één hoofdletter, één cijfer en één speciaal teken")
        newPassword = input("Nieuwe wachtwoord (Enter om te behouden): ")
        if (isPasswordValid(newPassword) or newPassword == ""):
            break
    cursor = connection.cursor()
    if role == Roles.Service_Engineer:
        if newPassword:
            cursor.execute("UPDATE Service_Engineers SET Password=? WHERE Username=?",
                           (Hash(newPassword), Encrypt(username)))
    else:
        if newPassword:
            cursor.execute("UPDATE System_Administrators SET Password=? WHERE Username=?",
                            (Hash(newPassword), Encrypt(username)))
    connection.commit()
    print("Wachtwoord bijgewerkt.")


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

        print("Account verwijderd. Je bent nu uitgelogd.")
        time.sleep(3)
        exit()  # Verlaat de applicatie na verwijderen
    else:
        print("Verwijdering geannuleerd.")


def show_logs(connection):
    while True:
        print("\n--- Reguliere logs ---")
        logs = readLog(connection.cursor())

        for log in logs:
            print(log)

        print("0. Terug naar menu")
        choice = input("Maak een keuze: ")
        if choice == "0":
            break


def show_suspicious_logs(connection, username):
    while True:
        print("\n--- Verdachte logs ---")
        logs = readSuspiciousLog(connection, username)

        for log in logs:
            print(log)

        print("0. Terug naar menu")
        choice = input("Maak een keuze: ")
        if choice == "0":
            break


def show_logs_menu(connection, username):
    while True:
        print("\n--- Bekijk logs ---")
        print("1. Bekijk de reguliere logs")
        if (checkIfUnreadSuspiciousLogs(connection, username)):
            print("2. Bekijk de verdachte logs ‼ ongelezen logs ‼")
        else:
            print("2. Bekijk de verdachte logs")
        print("0. Terug naar hoofdmenu")

        choice = input("Maak een keuze: ")
        if choice == "1":
            show_logs(connection)
        elif choice == "2":
            show_suspicious_logs(connection, username)
        elif choice == "0":
            break


def add_traveller(connection):
    print("\n--- Nieuwe Traveller toevoegen ---")
    first = input("Voornaam: ")
    last = input("Achternaam: ")
    
    birthday_str = ""
    while True:
        birthday_str = input("Geboortedatum (YYYY-MM-DD): ")
        try:
            birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Ongeldig datumformaat")

    gender = input("Geslacht: ")
    street = input("Straatnaam: ")
    
    number_str = ""
    while not number_str.isdigit() or int(number_str) <= 0:
        number_str = input("Huisnummer: ").strip()
        if not number_str.isdigit():
            print("Voer een positief getal in")
        elif int(number_str) <= 0:
            print("Huisnummer moet > 0 zijn")
    number = int(number_str)

    zip_code = ""
    while not isZipcodeValid(zip_code):
        zip_code = input("Postcode: ").strip().upper()
        if not isZipcodeValid(zip_code):
            print("Ongeldig formaat (gebruik 1234AB)")

    city_str = ""
    cities = [city.name for city in CityEnum]
    while city_str.strip().upper() not in cities:
        city_str = input(f"Woonplaats ({', '.join(cities)}): ").strip()
        if city_str.upper() not in cities:
            print("Kies uit de voorgedefinieerde steden")
    
    email = ""
    while not isEmailValid(email):
        email = input("E-mailadres: ").strip()
        if not isEmailValid(email):
            print("Ongeldig e-mailformaat")

    phone = ""
    while not isPhoneNumberValid(phone):
        phone = input("Mobiel nummer (8 cijfers): ").strip()
        if not isPhoneNumberValid(phone):
            print("Voer 8 cijfers in (bijv. 06123456)")
    
    
    license = ""
    while not isDriversLicenseValid(license):
        license = input("Rijbewijsnummer (XX1234567 of X12345678): ").strip().upper()
        if not isDriversLicenseValid(license):
            print("Ongeldig formaat (XX1234567 of X12345678)")

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM Travellers WHERE DrivingLicenseNumber = ?", (Encrypt(license),))
    if cursor.fetchone():
        print("Een traveller met dit e-rijbewijsnummer bestaat al.")
        return

    addTravellerToDatabase(connection, Traveller(
        Driving_License_Number=license,
        First_Name=first,
        Last_Name=last,
        Birthday=birthday,
        Gender=gender,
        Street_Name=street,
        House_Number=number,
        Zip_Code=zip_code,
        City=CityEnum[city_str.upper()],
        Email_Address=email,
        Mobile_Phone=phone
    ))
    connection.commit()
    print("Traveller succesvol toegevoegd.")


def update_traveller(connection):
    license = ""
    while not isDriversLicenseValid(license):
        license = input("\nVoer het rijbewijsnummer van de traveller in die je wilt wijzigen (XX1234567 of X12345678): ").strip().upper()
        if not isDriversLicenseValid(license):
            print("Ongeldig formaat (XX1234567 of X12345678)")

    cursor = connection.cursor()
    found = findTravellers(cursor, Driving_License_Number=license)
    if len(found) <= 0:
        print("Traveller niet gevonden.")
        return
    traveller = found[0]
    
    print("Laat een veld leeg om het ongewijzigd te laten.")
    first = input("Voornaam: ")
    last = input("Achternaam: ")

    birthday_str = ""
    while True:
        birthday_str = input("Geboortedatum (YYYY-MM-DD): ")
        if birthday_str == "":
            break

        try:
            birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Ongeldig datumformaat")

    gender = input("Geslacht: ")
    street = input("Straatnaam: ")

    number_str = ""
    while not number_str.isdigit() or int(number_str) <= 0:
        number_str = input("Huisnummer: ").strip()
        if number_str == "":
            
            break
        else:
            if not number_str.isdigit():
                print("Voer een positief getal in")
            elif int(number_str) <= 0:
                print("Huisnummer moet > 0 zijn")
            else:
                number = int(number_str)
    

    zip_code = ""
    while not isZipcodeValid(zip_code):
        zip_code = input("Postcode: ").strip().upper()
        if zip_code == "":
            break
        if not isZipcodeValid(zip_code):
            print("Ongeldig formaat (gebruik 1234AB)")

    email = ""
    while not isEmailValid(email):
        email = input("E-mailadres: ").strip()
        if email == "":
            break
        if not isEmailValid(email):
            print("Ongeldig e-mailformaat")

    phone = ""
    while not isPhoneNumberValid(phone):
        phone = input("Mobiel nummer (8 cijfers): ").strip()
        if phone == "":
            break
        if not isPhoneNumberValid(phone):
            print("Voer 8 cijfers in (bijv. 06123456)")

    city_str = ""
    cities = [city.name for city in CityEnum]
    while city_str.strip().upper() not in cities:
        city_str = input(f"Woonplaats ({', '.join(cities)}): ").strip()
        if city_str == "":
            break
        if city_str.upper() not in cities:
            print("Kies uit de voorgedefinieerde steden")

    
    fields = {
        "First_Name": first,
        "Last_Name": last,
        "Birthday": birthday if birthday_str!= "" else birthday_str,
        "Gender": gender,
        "Street_Name": street,
        "House_Number": number if number_str!= "" else number_str,
        "Zip_Code": zip_code,
        "City": CityEnum[city_str.upper()] if city_str!= "" else city_str,
        "Email_Address": email,
        "Mobile_Phone": phone,
        "Driving_License_Number": license
    }

    for key, value in fields.items():
        if value != "" and value is not None:
            setattr(traveller, key, value)

    updateTravellerInDatabase(connection, traveller)
    print("Gegevens bijgewerkt.")


def delete_traveller(connection):
    license = ""
    while not isDriversLicenseValid(license):
        license = input("\nVoer het rijbewijsnummer van de traveller in die je wilt wijzigen (XX1234567 of X12345678): ").strip().upper()
        if not isDriversLicenseValid(license):
            print("Ongeldig formaat (XX1234567 of X12345678)")

    cursor = connection.cursor()
    found = findTravellers(cursor, Driving_License_Number=license)
    if len(found) <= 0:
        print("Traveller niet gevonden.")
        return
    traveller = found[0]
    
    confirm = input(
        f"Weet je zeker dat je traveller met rijbewijsnummer '{license}' wilt verwijderen? (ja/nee): ")
    if confirm.lower() == "nee":
        print("Verwijdering geannuleerd.")
        return
    
    deleteTravellerFromDatabase(connection, license)

    print("Traveller verwijderd.")


def find_traveller(connection):
    print("")
    search_fields = []
    valid_fields = [
        "Driving_License_Number", "First_Name", "Last_Name", "Birthday", "Gender", "Street_Name",
        "House_Number", "Zip_Code", "City", "Email_Address", "Mobile_Phone"
    ]

    while True:
        if search_fields:
            print("\nHuidige zoekvelden:")
            for field, value in search_fields:
                print(f"{field}: {value}")
        print("\nTyp in 'voorbeeld_veld':'voorbeeld_zoek_value' voor de veld die u wilt opzoeken")
        print("Typ alleen 'zoek' om de query uittevoeren")
        print("Mogelijke velden:")
        print(", ".join(valid_fields))

        field = input()

        if field == "zoek":
            break

        if not(':' in field):
            print("\nOngeldige invoer, probeer opnieuw.")
            continue

        field, value = field.split(':', 1)
        field = field.strip()
        value = value.strip()

        if not (field in valid_fields):
            print("\nOngeldig veld, probeer opnieuw.")
            continue

        valid = True
        if field == "House_Number":
            try:
                int(value)
            except ValueError:
                print(f"{field} moet een geheel getal zijn.")
                valid = False
        if valid:
            #Remove old entry for veld if exists
            search_fields = [pair for pair in search_fields if pair[0] != field]
            search_fields.append((field, value))
        
    cursor = connection.cursor()
    args = {}
    for field, value in search_fields:
        if field == "House_Number":
            args[field] = int(value)
        else:
            args[field] = value
    foundTravellers = findTravellers(cursor, **args)
    printTravellersList(foundTravellers)
    
    
            
    



def add_service_engineer(connection):
    print("\n--- Nieuwe Service Engineer toevoegen ---")
    username = input("Gebruikersnaam: ")
    first_name = input("Voornaam: ")
    last_name = input("Achternaam: ")
    password = input("Wachtwoord: ")

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM Service_Engineers WHERE Username = ?", (Encrypt(username),))
    if cursor.fetchone():
        print("Deze gebruikersnaam bestaat al.")
        return

    cursor.execute("""
        INSERT INTO Service_Engineers (Username, Password, First_Name, Last_Name, Registration_date)
        VALUES (?, ?, ?, ?, ?)
    """, (Encrypt(username), Hash(password), Encrypt(first_name), Encrypt(last_name), date.today()))

    connection.commit()
    print("Service Engineer succesvol toegevoegd.")


def update_service_engineer(connection):
    username = input("\nVoer de gebruikersnaam in van de Service Engineer: ")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM Service_Engineers WHERE Username = ?", (Encrypt(username),))
    if not cursor.fetchone():
        print("Service Engineer niet gevonden.")
        return

    print("Laat een veld leeg om deze ongewijzigd te laten.")
    new_first = input("Nieuwe voornaam: ")
    new_last = input("Nieuwe achternaam: ")

    if new_first:
        cursor.execute("UPDATE Service_Engineers SET First_Name = ? WHERE Username = ?",
                       (Encrypt(new_first), Encrypt(username)))
    if new_last:
        cursor.execute("UPDATE Service_Engineers SET Last_Name = ? WHERE Username = ?",
                       (Encrypt(new_last), Encrypt(username)))

    connection.commit()
    print("Gegevens bijgewerkt.")


def delete_service_engineer(connection):
    username = input(
        "\nVoer de gebruikersnaam in van de Service Engineer die je wilt verwijderen: ")
    confirm = input(
        f"Weet je zeker dat je '{username}' wilt verwijderen? (ja/nee): ")
    if confirm.lower() != "ja":
        print("Verwijdering geannuleerd.")
        return

    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM Service_Engineers WHERE Username = ?", (Encrypt(username),))
    connection.commit()

    print("Service Engineer verwijderd.")


def reset_service_engineer_password(connection):
    username = input("\nGebruikersnaam van de Service Engineer: ")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM Service_Engineers WHERE Username = ?", (Encrypt(username),))
    if not cursor.fetchone():
        print("Service Engineer niet gevonden.")
        return

    new_password = input("Nieuw wachtwoord: ")
    if not new_password:
        print("Ongeldig wachtwoord.")
        return

    cursor.execute("UPDATE Service_Engineers SET Password = ? WHERE Username = ?",
                   (Hash(new_password), Encrypt(username)))
    connection.commit()

    print("Wachtwoord opnieuw ingesteld.")

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
    log(connection, "added new scooter", "system_admin", f"serial number: {serial_number}")



def update_scooter_menu(connection):
    serial = input("\nVoer het serienummer in van de scooter die je wilt wijzigen: ")
    cursor = connection.cursor()
    found = findScooters(cursor, Serial_Number=serial)
    if not found:
        print("Scooter niet gevonden.")
        return
    scooter = found[0]

    print("Laat velden leeg om ze ongewijzigd te laten.")

    brand = input("Nieuw merk: ")
    if brand != "":
        scooter.Brand = brand

    model = input("Nieuw model: ")
    if model != "":
        scooter.Model = model

    top_speed_input = ""
    while not top_speed_input.isnumeric() or int(top_speed_input) < 0:
        top_speed_input = input("Voer de nieuwe top speed van de scooter in, alleen nummer en grooter dan 0: ")
        if top_speed_input == "":
            break
        if not top_speed_input.isnumeric():
            print("Gebruik alleen maar nummers")
            continue
        if top_speed_input.isnumeric() and int(top_speed_input) < 0:
            print("Top speed moet grooter dan")
            continue
        scooter.Top_Speed = int(top_speed_input)
    
    # batt capp
    battery_capacity_input = ""
    while not battery_capacity_input.isnumeric() or int(battery_capacity_input) < 0:
        battery_capacity_input = input("Voer de nieuwe batterijcapaciteit de scooter in, alleen nummer en grooter dan 0: ")
        if battery_capacity_input == "":
            break
        if battery_capacity_input.isnumeric() and int(battery_capacity_input) > 0:
            scooter.Battery_Capacity = int(battery_capacity_input)

    # soc
    soc_input = ""
    while not soc_input.isnumeric() or not (0 <= int(soc_input) <= 100):
        soc_input = input("Voer de nieuwe State of Charge (0-100%) in: ")
        if soc_input == "":
            break
        if soc_input.isnumeric() and (0 <= int(soc_input) <= 100):
            scooter.State_of_Charge = int(soc_input)
    
    #target soc

    min_soc = float(scooter.Target_Range_SoC.split(",")[0].strip("min: ").strip("%"))
    max_soc = float(scooter.Target_Range_SoC.split(",")[1].strip("max: ").strip("%"))
    while True:
        min_soc_input = ""
        while not min_soc_input.isnumeric() or not (0 <= int(min_soc_input) <= 100):
            min_soc_input = input("Voer het minimale Target Range SoC in (0-100): ")
            if min_soc_input == "":
                break
            if min_soc_input.isnumeric() and (0 <= int(min_soc_input) <= 100):
                min_soc = int(min_soc_input)

        max_soc_input = ""
        while not max_soc_input.isnumeric() or not (0 <= int(max_soc_input) <= 100) or int(max_soc_input) < min_soc:
            max_soc_input = input(f"Voer het maximale Target Range SoC in (tussen {min_soc} en 100): ")
            if max_soc_input == "":
                break
            if max_soc_input.isnumeric() and (0 <= int(max_soc_input) <= 100) and int(max_soc_input) > min_soc:
                max_soc = int(max_soc_input)
        
        if min_soc_input == "" and max_soc_input == "":
                break
        if max_soc < min_soc:
            print("het minimale target range is grooter dan maximale range")
            continue
        
        current_min = float(scooter.Target_Range_SoC.split(",")[0].strip("min: ").strip("%"))
        current_max = float(scooter.Target_Range_SoC.split(",")[1].strip("max: ").strip("%"))
        if min_soc_input == "" and max_soc_input != "":
                scooter.Target_Range_SoC = f"min: {current_min}%, max: {max_soc}%"
                break
        if min_soc_input != "" and max_soc_input == "":
                scooter.Target_Range_SoC = f"min: {min_soc}%, max: {current_max}%"
                break
        if min_soc_input != "" and max_soc_input != "":
                scooter.Target_Range_SoC = f"min: {min_soc}%, max: {max_soc}%"
                break
    

    lat_valid = False
    while not lat_valid:
        try:
            lat = input("Nieuwe latitude in: ")
            if lat == "":
                break
            lat_float = float(lat)
            scooter.Location = (lat_float, scooter.Location[1])
            
            lat_valid = True
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")
    
    lon_valid = False
    while not lon_valid:
        try:
            lon = input("Nieuwe longitude in: ")
            if lon == "":
                break
            lon_float = float(lon)
            scooter.Location = (scooter.Location[0], lon_float)
            
            lon_valid = True
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")
    
    valid_oos = False
    while not valid_oos:
        out_of_service_input = input("Is de scooter buiten gebruik? (ja/nee): ").strip().lower()
        if out_of_service_input == "":
            break
        if out_of_service_input in ("ja", "nee"):
            scooter.Is_Out_Of_Service = out_of_service_input == "ja"
            valid_oos = True
        else:
            print("Ongeldige invoer, typ 'ja' of 'nee'.")
    valid_date = False

    while not valid_date:
        date_input = input("Voer de laatste onderhoudsdatum in (DD-MM-YYYY): ")
        if date_input == "":
            break
        try:
            scooter.Last_Maintenance_Date = datetime.strptime(date_input, "%d-%m-%Y").date()
            valid_date = True
        except ValueError:
            print("Ongeldige datum, probeer opnieuw.")


    updateScooterInDatabase(connection, scooter)

    print("Gegevens bijgewerkt.")


def delete_scooter_menu(connection):
    serial = input("\nVoer het serienummer in van de scooter die je wilt verwijderen: ")
    confirm = input(f"Weet je zeker dat je scooter '{serial}' wilt verwijderen? (ja/nee): ")
    if confirm.lower() != "ja":
        print("Verwijdering geannuleerd.")
        return

    cursor = connection.cursor()
    cursor.execute("DELETE FROM Scooters WHERE Serial_Number = ?", (serial,))
    connection.commit()

    print("Scooter verwijderd.")


def find_scooter_menu(connection:sqlite3.Connection):
    print("")
    search_fields = []
    valid_fields = [
        "Serial_Number", "Brand", "Model", "Top_Speed", "Battery_Capacity", "State_of_Charge",
        "Target_Range_SoC", "Is_Out_Of_Service",
    ]

    while True:
        if search_fields:
            print("\nHuidige zoekvelden:")
            for field, value in search_fields:
                print(f"{field}: {value}")
        print("\nTyp in 'voorbeeld_veld':'voorbeeld_zoek_value' voor de veld die u wilt opzoeken")
        print("Typ alleen 'zoek' om de query uittevoeren")
        print("Mogelijke velden:")
        print(", ".join(valid_fields))

        field = input()

        if field == "zoek":
            break

        if ':' in field:
            field, value = field.split(':', 1)
            field = field.strip()
            value = value.strip()
            if field in valid_fields:
                valid = True
                if field in ["Top_Speed", "Battery_Capacity", "State_of_Charge", "Mileage"]:
                    try:
                        int(value)
                    except ValueError:
                        print(f"{field} moet een geheel getal zijn.")
                        valid = False
                elif field == "Is_Out_Of_Service":
                    if value.lower() not in ["true", "false"]:
                        print(f"{field} moet 'true' of 'false' zijn.")
                        valid = False
                elif field == "Target_Range_SoC":
                    match = re.fullmatch(r"min:(\d+),\s*max:(\d+)", value)
                    if not match or int(match.group(1)) <= 0 or int(match.group(2)) <= 0:
                        print(f"{field} moet in het formaat 'min:x, max:x' zijn, waarbij x > 0.")
                        valid = False
                if valid:
                    #Remove old entry for veld if exists
                    search_fields = [pair for pair in search_fields if pair[0] != field]
                    search_fields.append((field, value))
            else:
                print("\nOngeldig veld, probeer opnieuw.")
        else:
            print("\nOngeldige invoer, probeer opnieuw.")

    cursor = connection.cursor()
    args = {}
    for veld, waarde in search_fields:
        if veld in ["Top_Speed", "Battery_Capacity", "State_of_Charge", "Mileage", "amount"]:
            args[veld] = int(waarde)
        elif veld == "Is_Out_Of_Service":
            args[veld] = True if waarde.lower() == "true" else False
        else:
            args[veld] = waarde
    foundScooters = findScooters(cursor, **args)
    printScootersList(foundScooters)
    print("0. Terug")

    while True:
        choice = input("Van welke scooter zou u meer willen weten?: ")
        if choice == "0":
            return
        
        if not choice.isnumeric():
            print("Invoer moet numeriek zijn")
            continue
        
        if  not(1 <= int(choice)) or not(int(choice) < len(foundScooters) + 1):
            print(f"Invoer moet tussen {1} en {len(foundScooters) + 1} zijn")
            continue

        print(foundScooters[int(choice)-1])