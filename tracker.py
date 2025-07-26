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

def delete_expense(expense_id):
    expenses = load_expenses()
    original_len = len(expenses)

    # Filter out the expense with matching ID
    expenses = [e for e in expenses if e["id"] != expense_id]

    if len(expenses) == original_len:
        print(f"❌ No expense found with ID {expense_id}.")
    else:
        save_expenses(expenses)
        print(f"🗑️ Expense with ID {expense_id} deleted successfully.")

from datetime import datetime

def show_summary(month=None):
    expenses = load_expenses()

    if month:
        try:
            month = int(month)
            if not (1 <= month <= 12):
                print("❗ Month must be between 1 and 12.")
                return
        except ValueError:
            print("❗ Invalid month. Please provide a number between 1 and 12.")
            return

        current_year = datetime.now().year
        filtered = [
            e for e in expenses
            if datetime.strptime(e["date"], "%Y-%m-%d").month == month and
               datetime.strptime(e["date"], "%Y-%m-%d").year == current_year
        ]
        total = sum(e["amount"] for e in filtered)
        print(f"📆 Total expenses for {datetime(1900, month, 1).strftime('%B')}: ${total:.2f}")
    else:
        total = sum(e["amount"] for e in expenses)
        print(f"💰 Total expenses: ${total:.2f}")

def update_expense(expense_id, new_description=None, new_amount=None):
    expenses = load_expenses()
    updated = False

    for expense in expenses:
        if expense["id"] == expense_id:
            if new_description:
                expense["description"] = new_description
            if new_amount is not None:
                if new_amount < 0:
                    print("❗ Amount cannot be negative.")
                    return
                expense["amount"] = new_amount
            updated = True
            break

    if updated:
        save_expenses(expenses)
        print("✅ Expense updated successfully.")
    else:
        print("❌ Expense not found.")



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

    elif sys.argv[1] == "delete":
        if "--id" in sys.argv:
            try:
                idx = sys.argv.index("--id")
                expense_id = int(sys.argv[idx + 1])
                delete_expense(expense_id)
            except (IndexError, ValueError):
                print("❗ Usage: python tracker.py delete --id <expense_id>")
        else:
            print("❗ Missing --id argument.")
        
    elif sys.argv[1] == "summary":
        if "--month" in sys.argv:
            idx = sys.argv.index("--month")
            if idx + 1 < len(sys.argv):
                show_summary(sys.argv[idx + 1])
        else:
            print("❗ Please provide a month number after --month")
    elif sys.argv[1] == "update":
        if "--id" in sys.argv:
            try:
                idx = sys.argv.index("--id")
                expense_id = int(sys.argv[idx + 1])
            except (IndexError, ValueError):
                print("❗ Please provide a valid ID after --id.")
                return

            new_desc = None
            new_amount = None

            if "--description" in sys.argv:
                desc_idx = sys.argv.index("--description")
                if desc_idx + 1 < len(sys.argv):
                    new_desc = sys.argv[desc_idx + 1]

            if "--amount" in sys.argv:
                amt_idx = sys.argv.index("--amount")
                try:
                    new_amount = float(sys.argv[amt_idx + 1])
                except (IndexError, ValueError):
                    print("❗ Invalid amount.")
                    return

            update_expense(expense_id, new_desc, new_amount)
        else:
            print("❗ Please provide an expense ID using --id")
    else:
        show_summary()


if __name__ == "__main__":
    main()
