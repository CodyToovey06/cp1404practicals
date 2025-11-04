from guitar import Guitar


def run_tests():
    """Tests Guitar class."""

    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {103}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {13}. Got {other.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


run_tests()
