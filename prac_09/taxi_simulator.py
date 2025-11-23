from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q(uit, c(hoose taxi, d(rive"


def main():
    print("Let's drive")
    print(MENU)
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    taxi_choice = 0

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            choose_taxi(taxis)
        elif choice == "d":
            if taxi_choice == 0:
                print("You need to choose a taxi before you can drive")
            else:
                pass
        else:
            print("Invalid option")

        choice = input(">>> ").lower()


def choose_taxi(taxis):
    """Display available taxis and returns chosen one."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return 0
    except ValueError:
        print("Invalid taxi choice")
        return 0


main()
