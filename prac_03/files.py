name = input("Enter your name: ")
out_file = open("name.txt", 'w')
print(f"Name: {name}", file=out_file)
out_file.close()


in_file = open("name.txt", 'r')
text = in_file.read()
in_file.close()
print(text)


with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(f"First number: {first_number}")
print(f"Second number: {second_number}")
print(f"They add up to: {first_number + second_number}")


total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        total += int(line)
print(f"Total of all numbers is: {total}")