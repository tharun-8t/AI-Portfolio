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


def main():
    while True:
        print("\n" + "=" * 50)
        print("                    THARUN")
        print("=" * 50)
        print("1. View Profile")
        print("2. View Projects")
        print("3. Exit")
        print("=" * 50)

        choice = input("Choose an option: ")

        if choice == "1":
            show_profile()
        elif choice == "2":
            show_projects()
        elif choice == "3":
            print("\nThanks for visiting. Keep building. 🚀")
            break
        else:
            print("\nInvalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()