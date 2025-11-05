from abc import ABC, abstractmethod

class CostCalculator(ABC):
    @abstractmethod
    def calculate_cost(self, duration_hours: float) -> float:
        pass

class SmallCostCalculator(CostCalculator):
    def calculate_cost(self, duration_hours: float) -> float:
        base_rate = 10
        if (duration_hours <= 3):
            return base_rate
        return base_rate + (duration_hours - 3) * 5

class MediumCostCalculator(CostCalculator):
    def calculate_cost(self, duration_hours: float) -> float:
        base_rate = 15
        if (duration_hours <= 3):
            return base_rate
        return base_rate + (duration_hours - 3) * 7

class LargeCostCalculator(CostCalculator):
    def calculate_cost(self, duration_hours: float) -> float:
        base_rate = 20
        if (duration_hours <= 3):
            return base_rate
        return base_rate + (duration_hours - 3) * 10