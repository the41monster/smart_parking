from threading import Lock

class ParkingLot:
    def __init__(self, lot_id, floors):
        self.lot_id = lot_id
        self.floors = floors
        self.lock = Lock()
    
    def allocate_spot(self, vehicle):
        with self.lock:
            for floor in self.floors:
                for spot in floor.spots_by_type.get(vehicle.get_type(), []):
                    if spot.is_free:
                        spot.assign(vehicle)
                        return spot
        return None
    
    def free_spot(self, spot):
        with self.lock:
            spot.free()
    
    def get_availability(self):
        return {
            floor.floor_id: floor.get_availability()
            for floor in self.floors
        }
    