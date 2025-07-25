import sys
import json
import os
from datetime import datetime

FILENAME = "expenses.json"

# 🔹 Create file if not present
def load_expenses():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            json.dump([], f)
    with open(FILENAME, "r") as f:
        return json.load(f)

# 🔹 Save expenses back to file
def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)

# 🔹 Add new expense
def add_expense(description, amount):
    expenses = load_expenses()
    new_id = 1 if not expenses else expenses[-1]["id"] + 1
    new_expense = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": float(amount)
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"✅ Expense added successfully (ID: {new_id})")

def list_expenses():
    expenses = load_expenses()

    if not expenses:
        print("📭 No expenses found.")
        return

    print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Amount'}")
    print("-" * 45)
    for expense in expenses:
        print(f"{expense['id']:<4} {expense['date']:<12} {expense['description']:<15} ${expense['amount']:.2f}")


# 🔹 Main CLI Handler
def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "add":
        if "--description" in sys.argv and "--amount" in sys.argv:
            try:
                desc_index = sys.argv.index("--description") + 1
                amt_index = sys.argv.index("--amount") + 1
                description = sys.argv[desc_index]
                amount = float(sys.argv[amt_index])
                if amount < 0:
                    print("❌ Amount cannot be negative.")
                else:
                    add_expense(description, amount)
            except (ValueError, IndexError):
                print("❗ Invalid usage. Please provide both description and amount.")
        else:
            print("❗ Usage: python tracker.py add --description <desc> --amount <amt>")
    
    elif sys.argv[1] == "list":
        list_expenses()
    
    else:
        print("❗ Unknown command. Supported: add")

    


if __name__ == "__main__":
    main()
