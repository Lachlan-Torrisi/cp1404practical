from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi calculations."""
    taxi = SilverServiceTaxi("FancyTaxi", 100, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    print(taxi)
    print(f"Fare = ${fare}")


main()
