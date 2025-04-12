from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class representing a generic vehicle."""

    def __init__(self, brand: str):
        self._brand = brand

    @abstractmethod
    def start_engine(self) -> None:
        """Start the vehicle engine (must be implemented by subclass)."""
        pass


class Bus(Vehicle):
    """Concrete class representing a bus, derived from Vehicle."""

    def __init__(self, brand: str, capacity: int):
        super().__init__(brand)
        self._capacity = capacity

    def start_engine(self) -> None:
        print(f"{self._brand} bus engine started with {self._capacity} seats.")

    def is_school_bus(self) -> bool:
        return True
