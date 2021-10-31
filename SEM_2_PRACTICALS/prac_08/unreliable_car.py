"""
CP1404 Practical
Unreliable Car class
"""
from SEM_2_PRACTICALS.prac_08.car import Car
import random

class UnreliableCar(Car):
    """Specialised verision of a Car with reliability attribute."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Generates a random number between 0 and 100 and only drive the car if that number is less than the car's reliability."""
        if random.randrange(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven