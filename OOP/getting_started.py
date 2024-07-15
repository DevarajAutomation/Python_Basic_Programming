class Car:
    vehicle_type = 'Commercial'

    def __init__(self, colour, engine):
        self.speed = None
        self.colour = colour
        self.engine = engine

    def display_property(self):
        return f" {self.speed}"

    def display_colour(self):
        return f"{self.colour} and {self.vehicle_type}"


class DieselCar(Car):
    def __init__(self, brand, engine_type, colour, speed):
        super().__init__(colour, speed)
        self.brand = brand
        self.engine_type = engine_type

    def test_colour(self):
        return self.colour, self.vehicle_type


car1 = Car('white', 45)
car2 = Car('blue', 35)
car3 = DieselCar('Suzuki', 'Four stroke', 'blue', 45)
car4 = DieselCar('Tata', 'two-stroke', 'red', 67)

print(car4.display_colour())
print(car4.test_colour())
