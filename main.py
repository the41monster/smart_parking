import time
from constants.vehicle_type import VehicleType
from constants.spot_type import SpotType
from models.parking_spot import ParkingSpot
from models.parking_floor import ParkingFloor
from services.parking_lot import ParkingLot
from services.entry_gate import EntryGate
from services.exit_gate import ExitGate
from models.vehicle_factory import SmallVehicleFactory, MediumVehicleFactory, LargeVehicleFactory


spots_small = [ParkingSpot(f"S-{i+1}", SpotType.SMALL) for i in range(6)]
spots_medium = [ParkingSpot(f"M-{i+1}", SpotType.MEDIUM) for i in range(5)]
spots_large = [ParkingSpot(f"L-{i+1}", SpotType.LARGE) for i in range(3)]

floor1 = ParkingFloor("F1", {
    SpotType.SMALL: spots_small,
    SpotType.MEDIUM: spots_medium,
    SpotType.LARGE: spots_large
})

parking_lot = ParkingLot("Lot1", [floor1])
entry_gate = EntryGate("Gate1", parking_lot)
exit_gate = ExitGate("Gate2", parking_lot)

vehicle_factories = {
    VehicleType.SMALL: SmallVehicleFactory(),
    VehicleType.MEDIUM: MediumVehicleFactory(),
    VehicleType.LARGE: LargeVehicleFactory()
}

v1 = vehicle_factories[VehicleType.SMALL].create_vehicle("KA-01-HH-1234")
v2 = vehicle_factories[VehicleType.MEDIUM].create_vehicle("KA-01-HH-9999")
v3 = vehicle_factories[VehicleType.LARGE].create_vehicle("KA-01-HH-0001")

ticket1 = entry_gate.create_ticket(v1)
ticket2 = entry_gate.create_ticket(v2)
ticket3 = entry_gate.create_ticket(v3)

print(f"Tickets issued: {ticket1.ticket_id}, {ticket2.ticket_id}, {ticket3.ticket_id}")
print("Current Parking Availability:", parking_lot.get_availability())

time.sleep(2)

cost1 = exit_gate.process_exit(ticket1)
cost2 = exit_gate.process_exit(ticket2)
cost3 = exit_gate.process_exit(ticket3)

print(f"{v1.vehicle_no} parking cost: {cost1}")
print(f"{v2.vehicle_no} parking cost: {cost2}")
print(f"{v3.vehicle_no} parking cost: {cost3}")

print("Current Parking Availability:", parking_lot.get_availability())
