




from Menus.Overlapping_Menu import own_profile_submenu, scooter_submenu, service_engineer_submenu, traveller_submenu


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
            own_profile_submenu()
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

