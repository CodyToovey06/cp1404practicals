from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option.")
        print(f"Bill to date ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost ${total_bill:.2f}")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Select taxi based on user input."""
    print("Taxis available:")
    display_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))

    try:
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
        return None


def display_taxis(taxis):
    """Display a list of taxis each with their own line."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_taxi, total_fare):
    """Drive taxi using Taxi and SilverServiceTaxi classes"""
    if current_taxi:
        current_taxi.start_fare()
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        total_fare += trip_cost
    else:
        print("You need to choose a taxi before you can drive")
    return total_fare


if __name__ == '__main__':
    main()
