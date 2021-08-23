"""CP1404 PRACTICAL 3 - PASSWORD CHECKER"""
MIN_PASSWORD_LENGTH = 10


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("What is the password you would like to set? ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print(f"that password is too short, please enter a password of {MIN_PASSWORD_LENGTH} characters or more.")
        password = input("What is the password you would like to set? ")
    return password


main()
