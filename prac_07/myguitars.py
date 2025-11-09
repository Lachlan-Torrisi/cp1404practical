from guitar import Guitar

def main():
    """Read guitars from file, store as objects, and display."""
    guitars = load_guitars("guitars.csv")
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    """Read guitars from file and store in a list."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars

main()