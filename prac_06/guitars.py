from guitar import Guitar


def main():
    """Store user’s guitars and display details."""
    print("My guitars!")
    guitars = []

    # Uncomment these lines while testing to avoid typing repeatedly
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")



if __name__ == "__main__":
    main()