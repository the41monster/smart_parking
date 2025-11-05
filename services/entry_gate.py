from models.parking_ticket import ParkingTicket

class EntryGate:
    def __init__(self, gate_id, parking_lot) -> None:
        self.gate_id = gate_id
        self.parking_lot = parking_lot
    
    def create_ticket(self, vehicle) -> ParkingTicket|None:
        spot = self.parking_lot.allocate_spot(vehicle)
        if not spot:
            print("No available parking spots for the vehicle type.")
            return None
        ticket = ParkingTicket(vehicle, spot)
        return ticket
    