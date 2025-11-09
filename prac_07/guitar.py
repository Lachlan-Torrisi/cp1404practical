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

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return the guitars age in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is VINTAGE_AGE years or older."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """
        Less than comparison based on guitar's year.
        Older guitars are considered 'less than' newer ones.
        """
        return self.year < other.year
