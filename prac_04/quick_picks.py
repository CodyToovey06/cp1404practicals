import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """"""
    number_of_quick_picks = get_valid_number()


def get_valid_number():
    """"""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Quick picks cannot be 0")
        number_of_quick_picks = int(input("How many quick picks? "))
    return number_of_quick_picks
