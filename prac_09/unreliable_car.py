from prac_09.car import Car
import random

class UnreliableCar(Car):
    """A car that's not always reliable."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Only drive the car if random number is less than reliability."""
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0