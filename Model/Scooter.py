from datetime import date


class Scooter:
    Brand: str
    Model: str
    # 10 to 17 alphanumeric characters
    Serial_Number: str
    Top_Speed: int
    Battery_Capacity: int
    # between 0 & 100 %
    State_of_Charge: int
    # The recommended operating range of the scooter's battery, defined by a minimum and maximum State of Charge (SoC).
    Target_Range_SoC: int
    # The current GPS coordinates (latitude and longitude) of the scooter. 
    # Must be a real-world location within the Rotterdam region.
    # 5 decimal places, e.g., latitude = 51.9225, longitude = 4.47917.
    # Location[0] = latitude, Location[1] = longitude
    Location: tuple[float,float]
    Is_Out_Of_Service: bool
    # The total distance travelled by the scooter since it was first used, measured in kilometres.
    Mileage: int
    Last_Maintenance_Date: date

    def __init__(
        self,
        Brand: str,
        Model: str,
        Serial_Number: str,
        Top_Speed: int,
        Battery_Capacity: int,
        State_of_Charge: int,
        Target_Range_SoC: int,
        Location: tuple[float, float],
        Is_Out_Of_Service: bool,
        Mileage: int,
        Last_Maintenance_Date: date
    ):
        self.Brand = Brand
        self.Model = Model
        self.Serial_Number = Serial_Number
        self.Top_Speed = Top_Speed
        self.Battery_Capacity = Battery_Capacity
        self.State_of_Charge = State_of_Charge
        self.Target_Range_SoC = Target_Range_SoC
        self.Location = Location
        self.Is_Out_Of_Service = Is_Out_Of_Service
        self.Mileage = Mileage
        self.Last_Maintenance_Date = Last_Maintenance_Date


