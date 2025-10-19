


def main():
    email_to_name = {}
    user_email = input("Email: ")

    while user_email != "":
        user_name = get_name_from_email(user_email)
        verification = input(f"Is your name {user_name}? (Y/n) ").upper()
        if verification != "" and verification != "Y":
            user_name = input("Name: ")
        print(user_name)

def get_name_from_email(user_email):
    prefix = user_email.split('@')[0]
    parts = prefix.replace('.', ' ').split()
    user_name = " ".join(parts).title()
    return user_name

main()