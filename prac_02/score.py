import random


def main():
    """Gets user entered score."""
    result = result_calculator(float(input("Enter score: ")))
    print(f"Your overall result is {result}")
    random_result = result_calculator(random.randint(0, 100))
    print(f"Random result generated: {random_result}")


def result_calculator(score):
    """Determine the result from the users score."""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "passable"
    else:
        result = "bad"

    return result


main()
