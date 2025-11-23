from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q(uit, c(hoose taxi, d(rive"

def main():
    print("Let's drive")
    print(MENU)
    choice = input(">>> ").lower()
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    taxi_choice = 0
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            if taxi_choice == 0:
                print("You need to choose a taxi before you can drive")
            else:
                pass
        else:
            print("Invalid option")
            

