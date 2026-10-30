
from pathlib import Path
import csv
import os

filename = Path(__file__).parent / "expenses.csv"


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")

    category = input("Enter category: ").strip().lower()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    description = input("Enter description: ")

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(filename) == 0:
            writer.writerow(["Date", "Category", "Amount", "Description"])

        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


def view_expenses():
    if not os.path.exists(filename):
        print("No expenses found.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def filter_expenses():
    category = input("Enter category to filter: ").strip().lower()

    if not os.path.exists(filename):
        print("No expenses found.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        found = False

        for row in reader:
            if row["Category"].strip().lower() == category:
                print(row)
                found = True

        if not found:
            print("No expenses found for this category.")


def category_summary():
    summary = {}

    if not os.path.exists(filename):
        print("No expenses found.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"].strip().lower()
            amount = float(row["Amount"])

            if category:
                summary[category] = summary.get(category, 0) + amount

    print("\nCategory Summary:")

    if not summary:
        print("No expenses found.")
    else:
        for category, total in summary.items():
            print(category, ":", round(total, 2))


while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        filter_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

