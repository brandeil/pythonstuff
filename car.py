class Car():
    """ my car class """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        self.fuel_level=self.fuel_capacity
        print("fuel tank is full.")

    def drive(self):
        print("the car is moving.")