from data.profile import NAME, ROLE, FOCUS
from projects.projects import PROJECTS


def show_profile():
    print("\n" + "=" * 50)
    print("                  THARUN'S PROFILE")
    print("=" * 50)
    print(f"Name     : {NAME}")
    print(f"Role     : {ROLE}")
    print("Focus    : " + " • ".join(FOCUS))
    print("=" * 50)


def show_projects():
    print("\n" + "=" * 50)
    print("                  PROJECTS")
    print("=" * 50)

    for number, project in enumerate(PROJECTS, start=1):
        print(f"\n{number}. {project['name']}")
        print(f"   Description : {project['description']}")
        print(f"   Status      : {project['status']}")

        print("   Technologies:")
        for technology in project["technologies"]:
            print(f"      • {technology}")

        print("   What I learned:")
        for lesson in project["learned"]:
            print(f"      • {lesson}")

        print(f"   Next        : {project['next']}")

    print("\n" + "=" * 50)


def explore_project():
    print("\n" + "=" * 50)
    print("              EXPLORE PROJECT")
    print("=" * 50)

    print("\nAvailable Projects:")

    for project in PROJECTS:
        print(f"{project['id']}. {project['name']}")

    print("=" * 50)

    choice = input("Choose a project (or press Enter to go back): ")

    if choice == "":
        return

    try:
        project_id = int(choice)
    except ValueError:
        print("\nInvalid choice.")
        return

    selected_project = None

    for project in PROJECTS:
        if project["id"] == project_id:
            selected_project = project
            break

    if selected_project is None:
        print("\nProject not found.")
        return

    print("\n" + "=" * 50)
    print(f"              {selected_project['name']}")
    print("=" * 50)

    print(f"\nDescription : {selected_project['description']}")
    print(f"Status      : {selected_project['status']}")

    print("\nTechnologies:")
    for technology in selected_project["technologies"]:
        print(f"  • {technology}")

    print("\nWhat I learned:")
    for lesson in selected_project["learned"]:
        print(f"  • {lesson}")

    print(f"\nNext        : {selected_project['next']}")

    print("\n" + "=" * 50)


def main():
    while True:
        print("\n" + "=" * 50)
        print("                    THARUN")
        print("=" * 50)
        print("1. View Profile")
        print("2. View Projects")
        print("3. Explore a Project")
        print("4. Exit")
        print("=" * 50)

        choice = input("Choose an option: ")

        if choice == "1":
            show_profile()

        elif choice == "2":
            show_projects()

        elif choice == "3":
            explore_project()

        elif choice == "4":
            print("\nThanks for visiting. Keep building. 🚀")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()