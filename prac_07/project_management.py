"""
Estimate: 5 hours
Actual time:
"""

from project import Project

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Project management program."""
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects(FILENAME)
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load projects from CSV file."""
    projects = []

    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    return projects


def display_projects(projects):
    """Display projects to user."""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not Project.is_complete(project)]
    for project in incomplete_projects:
        print(f" {project}")
    print("Complete projects:")
    complete_projects = [project for project in projects if Project.is_complete(project)]
    for project in complete_projects:
        print(f" {project}")


def save_projects(projects):
    """Save projects list to chosen file."""
    save_file = input("What file would you like to save to? ")
    with open(save_file, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                  f"\t{project.cost_estimation}\t{project.completion_percentage}", file=out_file)
        print(f"{len(projects)} projects saved to {save_file}")


def add_projects(projects):
    """Add new projects into list of projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = get_valid_number("Priority: ", 0, 10)
    cost_estimation = float(input("Cost Estimate: $"))
    completion_percentage = int(input("Percent Complete: "))
    projects.append(Project(name, start_date, priority, cost_estimation, completion_percentage))


def get_valid_number(prompt, low, high):
    """Get valid integer between low and high."""
    number = low
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            if number < low:
                print(f"Number must be > {low - 1}")
            elif number > high:
                print("Invalid number")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number


main()
