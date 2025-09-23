REQUIRED_LENGTH = 10


def main():
    """Password stars program"""
    password = get_password()
    print_stars(password)


def print_stars(password):
    """Print a number of * based on password length."""
    print("*" * len(password))


def get_password():
    """Get valid password from user."""
    password = input("Enter your password: ")
    while len(password) < REQUIRED_LENGTH:
        print("Password length invalid, please try again")
        password = input("Enter your password: ")
    return password


main()
