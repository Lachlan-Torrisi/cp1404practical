class Band:
    """Represents a band & list of musicians."""

    def __init__(self, name=""):
        """Construct a band with empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing."""
        return "\n".join(musician.play() for musician in self.musicians)
