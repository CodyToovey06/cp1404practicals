"""
CP1404/CP5632 Practical
Car class
"""
from taxi import Taxi


class SilverServiceTaxi (Taxi):
    """Specialised version of a Taxi that includes fare costs."""
    flagfall = 4.50

    def __init__(self, name, fanciness, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()


