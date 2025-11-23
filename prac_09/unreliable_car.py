from car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate reliability as well."""
        random_number = randint(0, 100)
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0
