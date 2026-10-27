class Vehicle:
    """Base class holding details common to all rentable vehicles."""
 
    def __init__(self, vehicle_id: str, base_rate: float):
        self._vehicle_id = vehicle_id
        self._base_rate = float(base_rate)
 
    def display_details(self) -> str:
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate:.2f}"
 
    def rental_charge(self) -> float:
        """Placeholder; subclasses override this."""
        return 0.0
 
 
class Car(Vehicle):
    """A car, charged by base rate multiplied by number of seats."""
 
    def __init__(self, vehicle_id: str, base_rate: float, num_seats: int):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats
 
    def rental_charge(self) -> float:
        return self._base_rate * self.num_seats
 
 
class Bike(Vehicle):
    """A bike, charged at half the base rate."""
 
    def __init__(self, vehicle_id: str, base_rate: float, bike_type: str):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type
 
    def rental_charge(self) -> float:
        return self._base_rate * 0.5
 
 
def calculate_rental(vehicle: Vehicle) -> float:
    """Return the daily rental charge for any Vehicle (polymorphism)."""
    return vehicle.rental_charge()
 
 
if __name__ == "__main__":
    fleet = [
        Car("CAR001", 100.00, 4),
        Car("CAR002", 80.00, 7),
        Bike("BIKE001", 40.00, "Scooter"),
        Bike("BIKE002", 60.00, "Motorcycle"),
        Vehicle("GEN001", 50.00),
    ]
 
    for v in fleet:
        print(v.display_details())
        print(f"  Daily rental charge: {calculate_rental(v):.2f}")
 

    