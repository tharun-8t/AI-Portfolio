import json
expenses = []
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []


def add_expense():
    name = input("Enter expense name: ")
    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses()
    print("\nExpense added successfully! ✅")

def delete_expense():
    if not expenses:
        print("\nNo expenses to delete.")
        return

    print("\n========== EXPENSES ==========")

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']} - ₹{expense['amount']:.2f}")

    print("==============================")

    try:
        choice = int(input("Enter expense number to delete: "))

        if choice < 1 or choice > len(expenses):
            print("\nInvalid expense number.")
            return

        removed = expenses.pop(choice - 1)
        save_expenses()

        print(f"\nDeleted: {removed['name']} ✅")

    except ValueError:
        print("\nPlease enter a valid number.")
def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n========== EXPENSES ==========")

    total = 0

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']}")
        print(f"   Amount   : ₹{expense['amount']:.2f}")
        print(f"   Category : {expense['category']}")

        total += expense["amount"]

    print("==============================")
    print(f"Total      : ₹{total:.2f}")
    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    print("\nCategory Totals:")

    for category, amount in category_totals.items():
        print(f"   {category:<12}: ₹{amount:.2f}")


def main():
    while True:
        print("\n==============================")
        print("      STUDENT EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        print("==============================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            print("\nThanks for using Expense Tracker. 👋")
            break

        else:
            print("\nInvalid option. Try again.")


if __name__ == "__main__":
    load_expenses()
    main()