from abc import ABC, abstractmethod

CURRENT_YEAR = 2025

class User(ABC):
    """Abstract blueprint for all website users."""
    
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year
        
    def account_age(self):
        """Return the account age in years (current year assumed to be 2025)"""
        return CURRENT_YEAR - self.account_year
    
    @abstractmethod
    def get_role(self):
        """Every subclass must return its role as a string."""
        pass
    
class Admin(User):
    def get_role(self):
        return "Admin"
    
    def __str__(self):
        return (f"Admin {self.name} has full access to the site"
                f"(account created in {self.account_year}).")
        
class Guest(User):
    def get_role(self):
        return "Guest"
    
    def __str__(self):
        return (f"Guest {self.name} has limited, read-only access"
                f"(account created in {self.account_year}).")
        
    
    