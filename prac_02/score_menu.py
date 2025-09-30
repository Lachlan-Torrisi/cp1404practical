LOW = 0
HIGH = 100
MENU = f"""(G)et a valid score (must be {LOW}-{HIGH} inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""


def main():
    """Main function that runs the score program. Runs the menu."""
    score = get_valid_number("Enter score: ", LOW, HIGH)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number("Enter score: ", LOW, HIGH)
        elif choice == "P":
            result = result_calculator(score)
            print(f"Your overall result is {result}")
        elif choice == "S":
            star_printer(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


def get_valid_number(prompt, low, high):
    """Checks whether the user entered number fits the requirements."""
    number = float(input(prompt))
    while number < low or number > high:
        print(f"Invalid input (Enter score between {low}-{high})")
        number = float(input(prompt))
    return number


def result_calculator(score):
    """Determine the result from the users score."""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def star_printer(number_of_stars):
    """Prints x amount of starts based of the user score."""
    number_of_stars = int(number_of_stars)
    for i in range(number_of_stars):
        print("*", end="")
    print()


main()
print("Farewell")
