class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days


class Car(Vehicle):
    def __init__(self, model, rental_rate, insurance_fee):
        super().__init__(model, rental_rate)
        self.insurance_fee = insurance_fee

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.insurance_fee


class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_fee):
        super().__init__(model, rental_rate)
        self.helmet_fee = helmet_fee

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.helmet_fee


class Truck(Vehicle):
    def __init__(self, model, rental_rate, cargo_charge):
        super().__init__(model, rental_rate)
        self.cargo_charge = cargo_charge

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.cargo_charge



print("=== Vehicle Rental System by Boobalan ===")

car1 = Car("TATA Punch", 1200, 800)
print("\nCar Model:", car1.model)
print("Rental for 3 days:", car1.calculate_rental(3))

bike1 = Bike("Apache", 500, 100)
print("\nBike Model:", bike1.model)
print("Rental for 2 days:", bike1.calculate_rental(2))
