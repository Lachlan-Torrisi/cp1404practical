from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A more fancy Taxi that charges more per km and includes a flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string representation with flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

