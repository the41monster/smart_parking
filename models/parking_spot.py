from models.vehicle import Vehicle

class ParkingSpot:
    def __init__(self, spot_id: str, size: str):
        self.spot_id = spot_id
        self.size = size
        self.is_free = True
        self.vehicle = None
    
    def assign(self, vehicle: Vehicle):
        if not self.is_free:
            raise Exception(f"Parking spot {self.spot_id} is already occupied.")
        self.vehicle = vehicle
        self.is_free = False
    
    def free(self):
        self.vehicle = None
        self.is_free = True
