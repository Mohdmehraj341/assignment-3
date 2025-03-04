class Vehicle:
    def __init__(self, brand, model, rent_per_day):
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day
        self.available = True 

    def display_info(self):
        """Displays vehicle details."""
        return f"{self.brand} {self.model} - Rent: ₹{self.rent_per_day}/day - {'Available' if self.available else 'Rented'}"

    def rent_vehicle(self):
        """Marks the vehicle as rented."""
        if self.available:
            self.available = False
            return f"{self.brand} {self.model} has been rented."
        return f"{self.brand} {self.model} is already rented."

    def return_vehicle(self):
        """Marks the vehicle as available."""
        if not self.available:
            self.available = True
            return f"{self.brand} {self.model} has been returned."
        return f"{self.brand} {self.model} was not rented."



class Car(Vehicle):
    def __init__(self, brand, model, rent_per_day, seats, fuel_type):
        super().__init__(brand, model, rent_per_day)
        self.seats = seats
        self.fuel_type = fuel_type

    def display_info(self):
        """Displays car details."""
        return (super().display_info() + 
                f" - Seats: {self.seats}, Fuel: {self.fuel_type}")



class Bike(Vehicle):
    def __init__(self, brand, model, rent_per_day, engine_cc):
        super().__init__(brand, model, rent_per_day)
        self.engine_cc = engine_cc

    def display_info(self):
        """Displays bike details."""
        return super().display_info() + f" - Engine: {self.engine_cc}cc"



car1 = Car("Toyota", "Camry", 2000, 5, "Petrol")
bike1 = Bike("Yamaha", "R15", 800, 150)


print(car1.display_info())
print(bike1.display_info())


print(car1.rent_vehicle())
print(car1.display_info())  


print(car1.return_vehicle())
print(car1.display_info())