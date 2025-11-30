class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, hourly_rate)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.salary * self.hours_worked


class Manager(Employee):
    def __init__(self, name, salary, incentives):
        super().__init__(name, salary)
        self.incentives = incentives

    def calculate_salary(self):
        return self.salary + self.incentives



print("=== Regular Employee ===")
emp1 = RegularEmployee("Boobalan", 30000, 5000)
print("Name:", emp1.name)
print("Calculated Salary:", emp1.calculate_salary())

print("\n=== Contract Employee ===")
emp2 = ContractEmployee("Boobalan", 1000, 20)
print("Name:", emp2.name)
print("Calculated Salary:", emp2.calculate_salary())

print("\n=== Manager ===")
emp3 = Manager("Boobalan", 50000, 10000)
print("Name:", emp3.name)
print("Calculated Salary:", emp3.calculate_salary())