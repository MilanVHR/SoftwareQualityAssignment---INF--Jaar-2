from datetime import datetime
from Controllers.Validations import isSerialNumberValid
from Model.Scooter import Scooter, addScooterToDatabase



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
            add_scooter_menu()
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

def add_scooter_menu():
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
        top_speed_input = input("Voer de top speed van de scooter in, alleen nummer:")
    top_speed = int(top_speed_input)
    
    battery_capacity_input = ""
    while not battery_capacity_input.isnumeric() or int(battery_capacity_input) < 0:
        battery_capacity_input = input("Voer de batterijcapaciteit de scooter in, alleen nummer:")
    battery_capacity = int(battery_capacity_input)

    battery_capacity_input = ""
    while not battery_capacity_input.isnumeric() or int(battery_capacity_input) < 0:
        battery_capacity_input = input("Voer de batterijcapaciteit de scooter in, alleen nummer:")
    battery_capacity = int(battery_capacity_input)

    soc_input = ""
    while not soc_input.isnumeric() or not (0 <= int(soc_input) <= 100):
        soc_input = input("Voer de State of Charge (0-100%) in:")
    state_of_charge = int(soc_input)

    min_soc = -1
    max_soc = -2
    while max_soc < min_soc:
        min_soc_input = ""
        while not min_soc_input.isnumeric() or not (0 <= int(min_soc_input) <= 100):
            min_soc_input = input("Voer het minimale Target Range SoC in (0-100):")
        min_soc = int(min_soc_input)

        max_soc_input = ""
        while not max_soc_input.isnumeric() or not (0 <= int(max_soc_input) <= 100) or int(max_soc_input) < min_soc:
            max_soc_input = input(f"Voer het maximale Target Range SoC in (tussen {min_soc} en 100):")
        max_soc = int(max_soc_input)
        if max_soc < min_soc:
            print("het minimale target range is grooter dan maximale range")
    target_range_soc = f"min: {min_soc}%, max: {max_soc}"

    location_valid = False
    while not location_valid:
        try:
            lat = float(input("Voer de latitude in:"))
            lon = float(input("Voer de longitude in:"))
            location = (lat, lon)
            location_valid = True
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")

    valid_oos = False
    while not valid_oos:
        out_of_service_input = input("Is de scooter buiten gebruik? (ja/nee):").strip().lower()
        if out_of_service_input in ("ja", "nee"):
            is_out_of_service = out_of_service_input == "ja"
            valid_oos = True
        else:
            print("Ongeldige invoer, typ 'ja' of 'nee'.")

    mileage_input = ""
    while not mileage_input.isnumeric() or int(mileage_input) < 0:
        mileage_input = input("Voer de kilometerstand in (alleen nummer):")
    mileage = int(mileage_input)

    valid_date = False
    while not valid_date:
        date_input = input("Voer de laatste onderhoudsdatum in (DD-MM-YYYY):")
        try:
            last_maintenance_date = datetime.strptime(date_input, "%d-%m-%Y").date()
            valid_date = True
        except ValueError:
            print("Ongeldige datum, probeer opnieuw.")

    toAdd = Scooter(serial_number, brand, model, top_speed, battery_capacity, state_of_charge, target_range_soc, location, is_out_of_service, mileage, last_maintenance_date)
    addScooterToDatabase(toAdd)

