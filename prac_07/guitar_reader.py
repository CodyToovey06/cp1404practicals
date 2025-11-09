from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Program that reads guitars from file and store them in a list of Guitar objects."""
    guitars = load_guitars(FILENAME)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")
        with open(FILENAME, 'a') as outfile:
            print(f"{name}, {cost}, {year}", file=outfile)
    guitars.sort()
    display_guitars(guitars)


def load_guitars(filename):
    """Read guitars from csv file."""
    guitars = []
    in_file = open(filename, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


def display_guitars(guitars):
    """Display Guitars."""
    for guitar in guitars:
        print(f"{guitar.name}, Year: {guitar.year}, Cost: ${guitar.cost}")

main()
