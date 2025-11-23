from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_fare = 0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            pass
        else:
            print("Invalid option.")
        print(MENU)
        choice = input(">>> ").lower()


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


if __name__ == '__main__':
    main()
