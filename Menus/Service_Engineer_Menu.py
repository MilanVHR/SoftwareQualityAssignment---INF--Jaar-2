from datetime import datetime
import sqlite3

from Controllers.Logging import log
from Database.DBCheckUser import Roles
from Menus.Overlapping_Menu import own_profile_submenu
from Model.Scooter import Scooter, findScooters, updateScooterInDatabase


def service_engineer_menu(connection, username):
    while True:
        print("\n=== SERVICE ENGINEER MENU ===")
        print("1. Beheer eigen profiel")
        print("2. Update scootergegevens (alleen toegestaan velden)")
        print("3. Zoek en bekijk scooterinformatie")
        print("0. Log uit")

        choice = input("Maak een keuze: ")

        if choice == "1":
            own_profile_submenu(connection, username, Roles.Service_Engineer)
        elif choice == "2":
            update_scooter_attributes(connection, username)
        elif choice == "3":
            search_scooter(username)
        elif choice == "0":
            print("Je bent uitgelogd.\n")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")



def update_scooter_attributes(connection, username):
    cursor = connection.cursor()

    print("\n--- Scootergegevens bijwerken (alleen toegestane velden) ---")
    serial_number = ""
    while len(serial_number) < 10  or len(serial_number) > 17:
        serial_number = input("Voer het serienummer van de scooter in: ")
        if len(serial_number) < 10:
            print("Serienummer moet grooter dan 10 zijn")
        if len(serial_number) > 17:
            print("Serienummer moet kleiner dan 17 zijn")
    
    scooters = findScooters(cursor, Serial_Number = serial_number)
    if len(scooters) > 0:
        scooter = scooters[0]
    else:
        print(f"\nGeen scooter gevonden met serienummer: {serial_number}")
        return

    print("Gevonden scooter:")
    print(f"Serienummer: {scooter.Serial_Number}")
    print(f"Brand: {scooter.Brand}")
    print(f"Model: {scooter.Model}")
    print(f"Top snelheid: {scooter.Top_Speed}")
    print(f"Batterij capaciteit: {scooter.Battery_Capacity}")
    print(f"State of charge: {scooter.State_of_Charge}")
    print(f"Werk target range state of charge: {scooter.Target_Range_SoC}")
    print(f"Locatie: {scooter.Location[0]}, {scooter.Location[1]}")
    print(f"Is buiten gebruik: {scooter.Is_Out_Of_Service}")
    print(f"Kilometerstand: {scooter.Mileage}")
    print(f"Laatste onderhoudsdatum: {str(scooter.Last_Maintenance_Date)}\n")

    while True:
        print("1. State of Charge (SoC) wijzigen")
        print("2. Locatie wijzigen (GPS-coördinaten)")
        print("3. Out-of-Service status wijzigen")
        print("4. Kilometerstand bijwerken")
        print("5. Laatste onderhoudsdatum bijwerken")
        print("0. Terug")

        choice = input("Welke eigenschap wil je bijwerken? ")

        if choice == "1":
            new_soc = ""
            while not new_soc.isnumeric() or int(new_soc) < 0 or int(new_soc) > 100:
                new_soc = input("Nieuwe SoC (%): ")
                if not new_soc.isnumeric():
                    print("")
                if len(new_soc) < 0:
                    print("Serienummer moet grooter dan 10 zijn")
                if len(new_soc) > 100:
                    print("Serienummer moet kleiner dan 17 zijn")
               # (nog te implementeren)

            log("Scooter: State of Charge updated", username, f"scooter serial number: {scooter.Serial_Number}, new SoC: {new_soc}")

            #DB-update
            scooter.State_of_Charge = new_soc
            updateScooterInDatabase(connection, scooter)
            print(f"SoC bijgewerkt naar {new_soc}%\n")
        
        elif choice == "2":
            #Latitude input loop
            latitude = ""
            while not latitude.replace('.', '', 1).replace('-', '', 1).isnumeric() or float(latitude) < -90 or float(latitude) > 90:
                latitude = input("Voer in latitude (-90 to 90): ")
                if not latitude.replace('.', '', 1).replace('-', '', 1).isnumeric():
                    print("Ingevoerde nummer is ongeldig.")
                elif float(latitude) < -90 or float(latitude) > 90:
                    print("Latitude moet zijn tussen -90 en 90.")

            #Longitude input loop
            longitude = ""
            while not longitude.replace('.', '', 1).replace('-', '', 1).isnumeric() or float(longitude) < -180 or float(longitude) > 180:
                longitude = input("Voer in longitude (-180 to 180): ")
                if not longitude.replace('.', '', 1).replace('-', '', 1).isnumeric():
                    print("Ingevoerde nummer is ongeldig.")
                elif float(longitude) < -180 or float(longitude) > 180:
                    print("Longitude moet zijn tussen -180 en 180.")

            log("Scooter: location updated", username, f"scooter serial number: {scooter.Serial_Number}, new latitude: {latitude}, new longitude: {longitude}")

            #DB-update
            scooter.Location = (float(latitude),float(longitude))
            updateScooterInDatabase(connection, scooter)
            print(f"Locatie bijgewerkt naar lat={latitude}, lon={longitude}")
        
        elif choice == "3":
            valid_oos = False
            while not valid_oos:
                out_of_service_input = input("Is de scooter buiten gebruik? (ja/nee): ").strip().lower()
                if out_of_service_input in ("ja", "nee"):
                    is_out_of_service = out_of_service_input == "ja"
                    valid_oos = True
                else:
                    print("Ongeldige invoer, typ 'ja' of 'nee'.")

            log("Scooter: status updated", username, f"scooter serial number: {scooter.Serial_Number}, is the scooter out of service: {is_out_of_service}")

            # DB-update
            scooter.Is_Out_Of_Service = is_out_of_service
            updateScooterInDatabase(connection, scooter)
            print(f"Out-of-service status ingesteld op {valid_oos}\n")
        
        elif choice == "4":
            km = ""
            while not km.isnumeric() or int(km) <= 0:
                km = input("Nieuwe kilometerstand: ")
                if not km.isnumeric():
                    print("Voer een geldig getal in.")
                elif int(km) <= 0:
                    print("Kilometerstand moet groter dan 0 zijn.")

            log("Scooter: kilometers updated", username, f"scooter serial number: {scooter.Serial_Number}, new km: {km}")

            # DB-update
            scooter.Mileage = km
            updateScooterInDatabase(connection, scooter)
            print(f"Kilometerstand bijgewerkt naar {km} km")
        
        elif choice == "5":
            date_str = ""
            while True:
                date_str = input("Nieuwe onderhoudsdatum (YYYY-MM-DD): ")
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Voer een geldige datum in (YYYY-MM-DD).")

            log("Scooter: service date updated", username, f"scooter serial number: {scooter.Serial_Number}, new date: {date}")

            # DB-update
            scooter.Last_Maintenance_Date = date.date()
            updateScooterInDatabase(connection, scooter)
            print(f"Laatste onderhoudsdatum bijgewerkt naar {date}")
        
        elif choice == "0":
            return
        else:
            print("Ongeldige keuze.")


def search_scooter():
    return
