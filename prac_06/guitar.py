"""
Estimate: 15 mins
Actual:

"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar with name, year, and cost."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self) -> int:
        """Return the guitars age in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self) -> bool:
        """Return True if the guitar is VINTAGE_AGE years or older."""
        return self.get_age() >= VINTAGE_AGE
