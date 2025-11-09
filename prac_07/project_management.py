"""
Estimate: 60 min
Actual:
"""

from project import Project
from datetime import datetime

DEFAULT_FILENAME = "projects.txt"


def main():
    """Run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    menu = ("- (L)oad projects\n"
            "- (S)ave projects\n"
            "- (D)isplay projects\n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit")

    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "l":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects(projects)
        elif choice == "a":
            pass
        elif choice == "u":
            pass
        else:
            print("Invalid Choice")
        print(menu)
        choice = input(">>> ").lower()

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file into a list of Project objects."""
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save current projects to a named file."""
    with open(filename, "w") as file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display complete and incomplete projects sorted by priority."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete_projects):
        print(f"  {project}")


def filter_projects(projects):
    """Filter projects by start date entered by the user."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = [p for p in projects if p.start_date > filter_date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


if __name__ == "__main__":
    main()
