import random

NUMBERS_PER_PICK = 6
MIN = 1
MAX = 45

num_picks = int(input("How many quick picks? "))

for i in range(num_picks):
    numbers = []

    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN, MAX)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()

    print(" ".join(f"{num:2}" for num in numbers))
