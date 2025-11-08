from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Read guitars from file and store them in a list of Guitar objects."""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    guitars = add_guitars(guitars)

    for guitar in guitars:
        print(guitar)


def add_guitars(guitars):
    """Add new guitars to list and file."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")
        with open(FILENAME, 'w') as outfile:
            print(guitars, file=outfile)
    guitars.sort()
    return guitars


main()
