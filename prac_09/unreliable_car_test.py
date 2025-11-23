from unreliable_car import UnreliableCar
import random


def main():
    """Run simple tests on the UnreliableCar."""
    for i in range(100):
        reliability = random.randint(0, 100)
        car = UnreliableCar(f"Car{i}", 100, reliability)
        distance_driven = car.drive(10)
        if distance_driven > 0:
            result = "SUCCESS"
        else:
            result = "FAIL"
        print(f"Car {i}: {reliability}% reliability: {result}")


main()
