MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    """Score program."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Get valid score from user."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def print_result(score):
    """Print result."""
    print(f"Score: {score} is {determine_result(score)}")


def determine_result(score):
    """Determine result based on valid score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print a number of stars based on score."""
    print("*" * score)


main()
