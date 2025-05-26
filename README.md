 Opdracht in het kort
Je moet een console-gebaseerd Python 3 programma maken dat het backend systeem voor Urban Mobility simuleert. De focus ligt op softwarebeveiliging (input validatie, encryptie, logging, authenticatie, autorisatie).

📋 Wat moet je bouwen?
Een backend systeem voor Urban Mobility, een scooterverhuurbedrijf in Rotterdam.

🔧 Hoofdtaken:
Console Interface voor drie rollen:

Super Administrator

System Administrator

Service Engineer

Gebruik van een SQLite3 database (via sqlite3 module in Python).

Encryptie van gevoelige data (zoals gebruikersnamen, adressen, telefoons, logs) via symmetrische encryptie.

Wachtwoorden hashen (geen wachtwoorden in platte tekst opslaan!).

👤 Gebruikersrollen & Toegangsrechten
Rol	Kan...
Super Admin	Alles. Mag ook System Admins aanmaken/verwijderen. Hardcoded login: super_admin / Admin_123?
System Admin	Scooters en travellers beheren, Service Engineers beheren, backups maken/herstellen, logs bekijken
Service Engineer	Alleen bestaande scooters bewerken en zoeken, en wachtwoord wijzigen

📦 Wat moet je systeem opslaan?
🧍 Traveller data:
Voornaam, achternaam, geboortedatum, geslacht, straat, huisnummer, postcode (formaat: DDDDXX), stad (10 vaste keuzes), e-mailadres, telefoonnummer (+31-6-DDDDDDDD), rijbewijsnummer (XXDDDDDDD of XDDDDDDDD)

Automatisch gegenereerde: registratiedatum + unieke klant-ID

🛵 Scooter data:
Merk, model, serienummer (10-17 tekens), topsnelheid, batterijcapaciteit, state-of-charge, target-range SOC, locatie (lat/lon in 5 decimalen), status, km-stand, laatste onderhoudsdatum

Automatisch gegenereerde: in-service datum

Let op: Sommige velden kunnen alleen door bepaalde rollen bewerkt worden (staat in een tabel in het document).

🔐 Beveiliging & Validatie
✅ Input Validatie:
Alle invoer moet worden gevalideerd (whitelisting, formaten, lengte, enz.)

🔒 Encryptie:
Encryptie van alle gevoelige velden via symmetrische encryptie.

Logbestanden moeten enkel via het systeem leesbaar zijn. Niet via teksteditor.

🧂 Hashing:
Wachtwoorden (behalve super admin) worden gehashed opgeslagen.

Gebruik een veilige hash-algoritme zoals bcrypt of hashlib + salt.

🧾 Logging:
Alle acties loggen.

Verdachte activiteiten markeren (zoals veel foute logins).

Logs moeten versleuteld worden opgeslagen.

💾 Backups
Backups in zip-formaat

Inhoud: database (inclusief encryptie)

System Admin mag alleen herstellen met een code die Super Admin genereert

Super Admin kan back-ups maken en restore-codes genereren/invullen

📜 Regels voor gebruikersnamen en wachtwoorden
🧑‍💻 Usernames:
8–10 tekens

Start met letter of _

Toegestane tekens: a-z, 0-9, _, ., '

Hoofdletterongevoelig

🔐 Passwords:
12–30 tekens

Moet 1 hoofdletter, 1 kleine letter, 1 cijfer en 1 speciaal teken bevatten

🧪 Eisen aan het programma
Moet foutloos draaien op standaard Windows/Mac met alleen:

Standaard bibliotheken

sqlite3, re en een gekozen encryptie/hash bibliotheek

Alle bestanden lokaal (zelfde folder of subfolder)

📁 Wat moet je inleveren?
.zip bestand: studentnummer1_studentnummer2_...

Bevat:

um_members.pdf: namen en studentnummers

Folder src/ met alle bestanden incl. um_members.py (de startfile)

📊 Beoordeling (Pass/Fail)
Je moet minimaal 10 punten halen en op deze onderdelen minstens Satisfactory scoren:

C1: Authenticatie & autorisatie

C2: Input validatie

C3: SQL-injectie bescherming

C4: Afhandeling ongeldige invoer

C5: Logging & backups

C6: Uitleg geven tijdens presentatie

📅 Deadline & Presentatie
Deadline eerste kans: 20 juni 2025

Presentatie verplicht (in Wijnhaven 107, planning via online formulier op Teams)

Geen slides nodig, alleen systeem draaien en uitleggen

✅ Wat je als eerst moet doen
Maak een duidelijke console-interface met login op basis van rollen

Zet je SQLite database structuur op

Voeg encryptie en hashing toe

Bouw stap voor stap de functionaliteiten per rol

Implementeer logging en backup

Test alles grondig!

Laat me weten als je hulp wilt met een specifiek onderdeel zoals:

De database opzetten

Inputvalidatie code

Encryptie of hashing

Structuur van je Python-code
