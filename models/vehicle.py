from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_no: str, vehicle_type: str, cost_calculator):
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type
        self.cost_calculator = cost_calculator
    
    def get_type(self) -> str:
        return self.vehicle_type
    
    def calculate_cost(self, duration_hours):
        return self.cost_calculator.calculate_cost(duration_hours)

class SmallVehicle(Vehicle):
    def __init__(self, vehicle_no: str, vehicle_type: str, cost_calculator):
        super().__init__(vehicle_no, vehicle_type, cost_calculator)

class MediumVehicle(Vehicle):
    def __init__(self, vehicle_no: str, vehicle_type: str, cost_calculator):
        super().__init__(vehicle_no, vehicle_type, cost_calculator)

class LargeVehicle(Vehicle):
    def __init__(self, vehicle_no: str, vehicle_type: str, cost_calculator):
        super().__init__(vehicle_no, vehicle_type, cost_calculator)
