def show_profile():
    print("\n" + "=" * 45)
    print("             THARUN'S PROFILE")
    print("=" * 45)
    print("Name     : Tharun")
    print("Role     : Student • Builder • Problem Solver")
    print("Focus    : Python • Programming • Projects")
    print("=" * 45)


def show_projects():
    print("\n" + "=" * 45)
    print("              PROJECTS")
    print("=" * 45)
    print("1. AI-Portfolio")
    print("   Personal portfolio project")
    print()
    print("More projects will be added as I build them.")
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