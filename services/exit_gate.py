class ExitGate:
    def __init__(self, gate_id: str, parking_lot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot

    def process_exit(self, ticket):
        ticket.close_ticket()
        duration = ticket.get_duration_hours()
        cost = ticket.vehicle.calculate_cost(duration)
        self.parking_lot.free_spot(ticket.spot)
        return cost