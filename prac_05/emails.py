"""
Emails
Estimate: 10 minutes
Actual:   11 minutes
"""


def main():
    """Creates dictionary of names from emails."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = determine_name_from_email(email)
        confirmation = input(f"Is this your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def determine_name_from_email(email):
    """Extract name from email"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
