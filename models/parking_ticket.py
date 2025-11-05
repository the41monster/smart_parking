from datetime import datetime
import uuid

class ParkingTicket:
    def __init__(self, vehicle, spot) -> None:
        self.ticket_id = str(uuid.uuid4())
        self.spot = spot
        self.vehicle = vehicle
        self.entry_time = datetime.now()
        self.exit_time = None
    
    def close_ticket(self) -> None:
        self.exit_time = datetime.now()
    
    def get_duration_hours(self) -> float:
        if not self.exit_time:
            raise Exception("Ticket is still open. Cannot calculate duration.")
        duration = self.exit_time - self.entry_time
        return duration.total_seconds() / 3600
    