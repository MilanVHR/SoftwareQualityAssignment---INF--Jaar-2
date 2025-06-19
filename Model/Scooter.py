from datetime import date, datetime
from sqlite3 import Connection


class Scooter:
    # 10 to 17 alphanumeric characters
    Serial_Number: str
    Brand: str
    Model: str
    Top_Speed: int
    Battery_Capacity: int
    # between 0 & 100 %
    State_of_Charge: int
    # The recommended operating range of the scooter's battery, defined by a minimum and maximum State of Charge (SoC).
    Target_Range_SoC: str
    # The current GPS coordinates (latitude and longitude) of the scooter. 
    # Must be a real-world location within the Rotterdam region.
    # 5 decimal places, e.g., latitude = 51.9225, longitude = 4.47917.
    # Location[0] = latitude, Location[1] = longitude
    Location: tuple[float,float]
    Is_Out_Of_Service: bool
    # The total distance travelled by the scooter since it was first used, measured in kilometres.
    Mileage: int
    Last_Maintenance_Date: date

    def __init__(self, Serial_Number: str, Brand: str, Model: str, Top_Speed: int, Battery_Capacity: int, State_of_Charge: int, Target_Range_SoC: int, Location: tuple[float, float], Is_Out_Of_Service: bool, Mileage: int, Last_Maintenance_Date: date):
        self.Serial_Number = Serial_Number
        self.Brand = Brand
        self.Model = Model
        self.Top_Speed = Top_Speed
        self.Battery_Capacity = Battery_Capacity
        self.State_of_Charge = State_of_Charge
        self.Target_Range_SoC = Target_Range_SoC
        self.Location = Location
        self.Is_Out_Of_Service = Is_Out_Of_Service
        self.Mileage = Mileage
        self.Last_Maintenance_Date = Last_Maintenance_Date

    def __str__(self):
        return (f"Serienummer: {self.Serial_Number}, Brand: {self.Brand}, Model: {self.Model}, "
                f"Top snelheid: {self.Top_Speed}, Batterij capaciteit: {self.Battery_Capacity}, Laadstatus: {self.State_of_Charge}, "
                f"Gewenste laadstatus: {self.Target_Range_SoC}, Locatie: {self.Location}, Is buiten gebruik: {self.Is_Out_Of_Service}, "
                f"Kilometerstand: {self.Mileage}, Laatste onderhoudsdatum: {self.Last_Maintenance_Date})")

def addScooterToDatabase(connection:Connection, scooter:Scooter):
    connection.cursor().execute("""
        INSERT INTO Scooters 
            (Serial_Number, Brand, Model, Top_Speed, Battery_Capacity, State_of_Charge, Target_Range_SoC, Location, Is_Out_Of_Service, Mileage, Last_Maintenance_Date) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
        (scooter.Serial_Number, scooter.Brand, scooter.Model, 
        scooter.Top_Speed, scooter.Battery_Capacity,scooter.State_of_Charge, 
        scooter.Target_Range_SoC, f"{scooter.Location[0]}, {scooter.Location[1]}", scooter.Is_Out_Of_Service,
        scooter.Mileage, f"{scooter.Last_Maintenance_Date}"))
    connection.commit()

def deleteScooterFromDatabase(connection:Connection, Serial_Number: int):
    connection.cursor().execute("DELETE FROM Scooters WHERE Serial_Number = ?", (Serial_Number,))
    connection.commit()

def updateScooterInDatabase(connection: Connection, scooter: Scooter):
    connection.cursor().execute("""UPDATE Scooters
        SET Brand = ?, Model = ?, Top_Speed = ?, Battery_Capacity = ?, State_of_Charge = ?, Target_Range_SoC = ?, Location = ?, Is_Out_Of_Service = ?, Mileage = ?, Last_Maintenance_Date = ?
        WHERE Serial_Number = ?""", 
        (scooter.Brand, scooter.Model, scooter.Top_Speed, scooter.Battery_Capacity, scooter.State_of_Charge, scooter.Target_Range_SoC, f"{scooter.Location[0]}, {scooter.Location[1]}", scooter.Is_Out_Of_Service, scooter.Mileage, f"{scooter.Last_Maintenance_Date}", scooter.Serial_Number))
    connection.commit()

def findScooters(cursor, Serial_Number=None, Brand=None, Model=None, Top_Speed=None, Battery_Capacity=None, State_of_Charge=None, Target_Range_SoC=None, Location=None, Is_Out_Of_Service=None, Mileage=None, Last_Maintenance_Date=None, amount=None) -> list[Scooter]:
    query = "SELECT * FROM Scooters"
    conditions = []
    params = []

    # Partial match for string columns using LIKE and wildcards
    if Serial_Number is not None:
        conditions.append("Serial_Number LIKE ?")
        params.append(f"%{Serial_Number}%")
    if Brand is not None:
        conditions.append("Brand LIKE ?")
        params.append(f"%{Brand}%")
    if Model is not None:
        conditions.append("Model LIKE ?")
        params.append(f"%{Model}%")
    if Target_Range_SoC is not None:
        conditions.append("Target_Range_SoC LIKE ?")
        params.append(f"%{Target_Range_SoC}%")
    if Location is not None:
        conditions.append("Location LIKE ?")
        params.append(f"%{Location}%")

    # Exact match for numeric, boolean, and date columns
    if Top_Speed is not None:
        conditions.append("Top_Speed = ?")
        params.append(Top_Speed)
    if Battery_Capacity is not None:
        conditions.append("Battery_Capacity = ?")
        params.append(Battery_Capacity)
    if State_of_Charge is not None:
        conditions.append("State_of_Charge = ?")
        params.append(State_of_Charge)
    if Is_Out_Of_Service is not None:
        conditions.append("Is_Out_Of_Service = ?")
        params.append(Is_Out_Of_Service)
    if Mileage is not None:
        conditions.append("Mileage = ?")
        params.append(Mileage)
    if Last_Maintenance_Date is not None:
        conditions.append("Last_Maintenance_Date = ?")
        params.append(Last_Maintenance_Date)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    if amount is not None:
        query += " LIMIT ?"
        params.append(amount)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    scooters = []
    
    for row in rows:
        (Serial_Number, Brand, Model, Top_Speed, Battery_Capacity, State_of_Charge, Target_Range_SoC, Location_str, Is_Out_Of_Service, Mileage, Last_Maintenance_Date
        ) = row
        latitude, longitude = map(float, Location_str.split(","))
        Location_tuple = (latitude, longitude)
        Last_Maintenance_Date = datetime.strptime(Last_Maintenance_Date, "%Y-%m-%d").date()
        
        scooter = Scooter(Serial_Number=Serial_Number, Brand=Brand, Model=Model, Top_Speed=Top_Speed, Battery_Capacity=Battery_Capacity, State_of_Charge=State_of_Charge, Target_Range_SoC=Target_Range_SoC, Location=Location_tuple, Is_Out_Of_Service=bool(Is_Out_Of_Service), Mileage=Mileage, Last_Maintenance_Date=Last_Maintenance_Date)
        scooters.append(scooter)

    return scooters 

def printScootersList(scooters: list[Scooter]):
    for i, scooter in enumerate(scooters, start=1):
        print(f"{i}. Serienummer: {scooter.Serial_Number}, Brand: {scooter.Brand}, Model: {scooter.Model}, Laatste onderhoudsdatum: {scooter.Last_Maintenance_Date}")