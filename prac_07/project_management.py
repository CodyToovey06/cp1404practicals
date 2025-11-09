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
    display_projects(projects)


def load_projects(filename):
    """Load projects from CSV file."""
    projects = []

    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            print(len(parts))
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


main()
