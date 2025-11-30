class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number   # encapsulation
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.get_balance() * self.interest_rate


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, min_balance=500):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.min_balance:
            super().withdraw(amount)
        else:
            print("Withdrawal denied! Minimum balance requirement not met.")



print("=== Savings Account ===")
s1 = SavingsAccount("ACC001", 2000, 0.05)
print("Balance:", s1.get_balance())
print("Interest Earned:", s1.calculate_interest())

print("\n=== Current Account ===")
c1 = CurrentAccount("ACC002", 1500, 500)
print("Balance:", c1.get_balance())
c1.withdraw(800)
print("Balance after withdrawing 800:", c1.get_balance())
c1.withdraw(300)