"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_data(FILENAME)
    print_data(subject_data)



def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_data.append(parts)
        print("----------")
    input_file.close()
    return subject_data


def print_data(subject_data):
    for subject in subject_data:
        print("{} is taught by {} and has {} students".format(subject[0], subject[1], subject[2]))

main()