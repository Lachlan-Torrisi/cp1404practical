from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from file, store as objects, and display."""
    guitars = load_guitars(FILENAME)
    guitars = add_new_guitars(guitars)

    guitars.sort(key=lambda guitar: guitar.year)
    print("These are my guitars (sorted by year)")
    for guitar in guitars:
        print(guitar)
    save_guitars(guitars, FILENAME)


def load_guitars(filename):
    """Read guitars from file and store in a list."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def add_new_guitars(guitars):
    """Prompt the user to enter a new guitar and append them to the list."""
    name = input("Guitar Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Guitar Name: ")

    return guitars


def save_guitars(guitars, filename):
    """Save guitars to CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
