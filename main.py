from data.profile import NAME, ROLE, FOCUS
from projects.projects import PROJECTS


def show_profile():
    print("\n" + "=" * 45)
    print("             THARUN'S PROFILE")
    print("=" * 45)
    print(f"Name     : {NAME}")
    print(f"Role     : {ROLE}")
    print("Focus    : " + " • ".join(FOCUS))
    print("=" * 45)


def show_projects():
    print("\n" + "=" * 45)
    print("              PROJECTS")
    print("=" * 45)

    for number, project in enumerate(PROJECTS, start=1):
        print(f"{number}. {project['name']}")
        print(f"   {project['description']}")
        print(f"   Status: {project['status']}")
        print()

    print("=" * 45)


def main():
    while True:
        print("\n" + "=" * 45)
        print("              THARUN")
        print("=" * 45)
        print("1. View Profile")
        print("2. View Projects")
        print("3. Exit")
        print("=" * 45)

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