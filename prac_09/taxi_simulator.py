from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q(uit, c(hoose taxi, d(rive"


def main():
    """Taxi simulator program."""
    print("Let's drive")
    print(MENU)
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    user_taxi = 0
    total_bill = 0

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            user_taxi = choose_taxi(taxis)
        elif choice == "d":
            if user_taxi == 0:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill += drive_taxi(user_taxi)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: {total_bill}")
    print("Taxis are now: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


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


def drive_taxi(user_taxi):
    """Drive the taxi for distance and returns cost."""
    distance = int(input("Drive how far? "))
    user_taxi.start_fare()
    user_taxi.drive(distance)
    trip_cost = user_taxi.get_fare()
    print(f"Your {user_taxi.name} trip cost you ${trip_cost}")

    return trip_cost


main()
