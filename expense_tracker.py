import csv
import os

FILE_NAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category"])


# Add expense
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (food, travel, etc): ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])

    print("Expense added successfully!\n")


# View all expenses
def view_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        print("\nAll Expenses:")
        for row in reader:
            print(f"Amount: {row[0]}, Category: {row[1]}")
    print()


# Calculate total expense (Calculator)
def calculate_total():
    total = 0
    category_total = {}

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            try:
                amount = float(row[0])
                category = row[1]

                total += amount

                # Category-wise calculation
                if category in category_total:
                    category_total[category] += amount
                else:
                    category_total[category] = amount

            except:
                print("Skipping invalid data")

    print("\nTotal Expense:", total)

    print("\nCategory-wise Expenses:")
    for cat, amt in category_total.items():
        print(f"{cat}: ₹{amt}")

# Menu
def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


main()