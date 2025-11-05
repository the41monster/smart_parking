from abc import ABC, abstractmethod
from constants.vehicle_type import VehicleType
from models.vehicle import Vehicle, SmallVehicle, MediumVehicle, LargeVehicle
from services.cost_calculator import SmallCostCalculator, MediumCostCalculator, LargeCostCalculator

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, vehicle_no: str) -> Vehicle:
        pass

class SmallVehicleFactory(VehicleFactory):
    def create_vehicle(self, vehicle_no: str) -> Vehicle:
        return SmallVehicle(vehicle_no, VehicleType.SMALL, SmallCostCalculator())

class MediumVehicleFactory(VehicleFactory):
    def create_vehicle(self, vehicle_no: str) -> Vehicle:
        return MediumVehicle(vehicle_no, VehicleType.MEDIUM, MediumCostCalculator())

class LargeVehicleFactory(VehicleFactory):
    def create_vehicle(self, vehicle_no: str) -> Vehicle:
        return LargeVehicle(vehicle_no, VehicleType.LARGE, LargeCostCalculator())