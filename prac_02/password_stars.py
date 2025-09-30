MIN_LENGTH = 8


def main():
    """Gets password and prints it."""
    password = get_password()
    print_password(password)


def print_password(password):
    """Prints user password as asteriks."""
    print("*" * len(password))


def get_password():
    """Gets user password (Checking password length)"""
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password is too short. (minimun length: {MIN_LENGTH} characters)")
        password = input("Password: ")
    return password


main()
