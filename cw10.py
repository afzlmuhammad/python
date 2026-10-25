from abc import ABC, abstractmethod

CURRENT_YEAR = 2025


class User(ABC):
    """Abstract base class: cannot be instantiated directly."""

    def __init__(self, name: str, joining_year: int):
        self.name = name
        self.joining_year = joining_year

    def years_on_platform(self) -> int:
        """Years since the user joined (current year assumed to be 2025)."""
        return CURRENT_YEAR - self.joining_year

    @abstractmethod
    def get_role(self) -> str:
        """Each subclass must report its own role."""

    def __str__(self) -> str:
        return (f"Name: {self.name} | Role: {self.get_role()} | "
                f"Years on platform: {self.years_on_platform()}")


class Customer(User):
    def get_role(self) -> str:
        return "Customer"


class Vendor(User):
    def get_role(self) -> str:
        return "Vendor"


if __name__ == "__main__":
    # User("Test", 2020) would raise TypeError: can't instantiate abstract class
    try:
        User("Test", 2020)
    except TypeError as e:
        print("Cannot create User directly ->", e)

    users = [Customer("Alice", 2021), Vendor("Bob", 2018), Customer("Carol", 2025)]
    for u in users:
        print(u)