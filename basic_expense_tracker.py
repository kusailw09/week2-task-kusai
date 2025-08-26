import csv
import os

FILENAME = "expense_tracker.csv"

# Initialize file with headers if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Description"])  # Headers

def add_record(record_type, amount, description=""):
    """Add income or expense record to CSV file"""
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([record_type, amount, description])
    print(f"{record_type} of {amount} added successfully!")

def show_summary():
    """Show total income, expenses and net balance"""
    total_income = 0
    total_expense = 0

    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Type"].lower() == "income":
                total_income += float(row["Amount"])
            elif row["Type"].lower() == "expense":
                total_expense += float(row["Amount"])

    net_balance = total_income - total_expense
    print("\n--- Summary ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Net Balance: {net_balance}")

# Simple menu
while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        desc = input("Enter description: ")
        add_record("Income", amount, desc)

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        desc = input("Enter description: ")
        add_record("Expense", amount, desc)

    elif choice == "3":
        show_summary()

    elif choice == "4":
        print("Exiting Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")