import sqlite3

from Menus.Overlapping_Menu import own_profile_submenu


def service_engineer_menu():
    while True:
        print("\n=== SERVICE ENGINEER MENU ===")
        print("1. Beheer eigen profiel")
        print("2. Update scootergegevens (alleen toegestaan velden)")
        print("3. Zoek en bekijk scooterinformatie")
        print("0. Log uit")

        choice = input("Maak een keuze: ")

        if choice == "1":
            own_profile_submenu()  # (nog te implementeren)
        elif choice == "2":
            update_scooter_attributes()
        elif choice == "3":
            search_scooter()
        elif choice == "0":
            print("Je bent uitgelogd.")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")





def update_scooter_attributes():
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
        new_soc = input("Nieuwe SoC (%): ")  # (nog te implementeren)
        #  DB-update
        print(f"SoC bijgewerkt naar {new_soc}%")
    elif choice == "2":
        # (nog te implementeren)
        lat = input("Nieuwe latitude (bijv. 51.9225): ")
        lon = input("Nieuwe longitude (bijv. 4.47917): ")
        #  DB-update
        print(f"Locatie bijgewerkt naar lat={lat}, lon={lon}")
    elif choice == "3":
        # (nog te implementeren)
        status = input("Is de scooter out-of-service? (ja/nee): ")
        #  DB-update
        print(f"Out-of-service status ingesteld op {status}")
    elif choice == "4":
        km = input("Nieuwe kilometerstand: ")  # (nog te implementeren)
        #  DB-update
        print(f"Kilometerstand bijgewerkt naar {km} km")
    elif choice == "5":
        # (nog te implementeren)
        date = input("Nieuwe onderhoudsdatum (YYYY-MM-DD): ")
        #  DB-update
        print(f"Laatste onderhoudsdatum bijgewerkt naar {date}")
    elif choice == "0":
        return
    else:
        print("Ongeldige keuze.")


def search_scooter():
    return
