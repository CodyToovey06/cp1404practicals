"""
Estimate: 5 hours
Actual time:
"""

from project import Project

FILENAME = "what.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Project management program."""
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    display_projects(projects)


def load_projects(filename):
    """Load projects from CSV file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('    ')
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    return projects


def display_projects(projects):
    """Display projects to user."""


main()
