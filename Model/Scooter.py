from datetime import date
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

def addScooterToDatabase(connection:Connection, scooter:Scooter):
    connection.cursor().execute("""
        INSERT INTO Scooters 
            (Serial_Number, Brand, Model, Top_Speed, Battery_Capacity, State_of_Charge, Target_Range_SoC, Location, Is_Out_Of_Service, Mileage, Last_Maintenance_Date) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, 
    (scooter.Serial_Number, scooter.Brand, scooter.Model, 
    scooter.Top_Speed, scooter.Battery_Capacity,scooter.State_of_Charge, 
    scooter.Target_Range_SoC, f"{scooter.Location[0]}, {scooter.Location[1]}", scooter.Is_Out_Of_Service,
    scooter.Mileage, f"{scooter.Last_Maintenance_Date}"))
    connection.commit()

def deleteScooterFromDatabase(connection:Connection, Serial_Number: int):
    connection.cursor().execute("DELETE FROM Scooters WHERE Serial_Number = ?", (Serial_Number,))
    connection.commit()

