class Account:
    """Base class storing the holder's name and balance (protected)."""
 
    def __init__(self, name: str, balance: float):
        self._name = name
        self._balance = float(balance)
 
    def __add__(self, other):
        """Adding two accounts returns the sum of their balances."""
        if not isinstance(other, Account):
            return NotImplemented
        return self._balance + other._balance
 
 
class SavingsAccount(Account):
    def calculate_interest(self) -> float:
        return self._balance * 0.05  # 5% interest
 
 
class CurrentAccount(Account):
    def calculate_interest(self) -> float:
        return self._balance * 0.02  # 2% interest
 
 
if __name__ == "__main__":
    ravi = SavingsAccount("Ravi", 10000)
    anjali = CurrentAccount("Anjali", 15000)
 
    for label, acc in (("Savings Account", ravi), ("Current Account", anjali)):
        print(f"--- {label} ---")
        print(f"Name:     {acc._name}")
        print(f"Balance:  {acc._balance:.2f}")
        print(f"Interest: {acc.calculate_interest():.2f}")
        print()
 
    total = ravi + anjali
    print(f"Total Balance (Ravi + Anjali): {total:.2f}")
 
