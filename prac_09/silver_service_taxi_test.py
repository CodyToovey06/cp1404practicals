from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Silver Taxi", 2, 100)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
