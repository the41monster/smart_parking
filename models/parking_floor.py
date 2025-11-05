from threading import Lock

class ParkingFloor:
    def __init__(self, floor_id, spots_by_type):
        self.floor_id = floor_id
        self.spots_by_type = spots_by_type
        self.lock = Lock()
    
    def asssign_spot(self, vehicle):
        with self.lock:
            for spot in self.spots_by_type.get(vehicle.get_type(), []):
                if spot.is_free:
                    spot.assign(vehicle)
                    return spot
        return None
    
    def get_availability(self):
        return {
            size: sum(1 for spot in spots if spot.is_free)
            for size, spots in self.spots_by_type.items()
        }