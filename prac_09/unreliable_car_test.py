from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCars."""

    good_car = UnreliableCar("Good Car", 100, 100)
    decent_car = UnreliableCar("Decent Car", 100, 50)
    bad_car = UnreliableCar("Bad Car", 100, 5)

    good_success = 0
    decent_success = 0
    bad_success = 0
    for i in range(1, 11):
        print(f"Try drive cars {i}km:")
        print(f"{good_car.name} drove {good_car.drive(i)}km")
        print(f"{decent_car.name} drove {decent_car.drive(i)}km")
        print(f"{bad_car.name} drove {bad_car.drive(i)}km")
        print()

        if good_car.drive(i) == i:
            good_success += 1
        if decent_car.drive(i) == i:
            decent_success += 1
        if bad_car.drive(i) == i:
            bad_success += 1

    print(f"Good: {good_success}/{i}, Decent: {decent_success}/{i}, Bad: {bad_success}/{i}")
    print(good_car)
    print(bad_car)


main()
