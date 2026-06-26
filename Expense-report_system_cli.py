import csv
import json
import datetime

transaction_file = "transactions.csv"
budget_file = "budget.json"

BUDGET_CATEGORIES = [
    "housing", "utilities", "transportation", "food",
    "health", "personal care", "lifestyle", "leisure",
]

REQUIRED_FIELDS = ["transaction_type", "category", "amount", "description", "date"]


# ----------------------------- LOAD / SAVE -----------------------------

def load_transactions():
    """Load transactions from CSV. Converts amount to float and skips
    malformed rows (missing fields, bad amount) with a warning instead
    of crashing. Returns [] if the file doesn't exist or is unreadable."""
    transactions = []
    try:
        with open(transaction_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):  # row 1 = header
                if row is None:
                    continue
                missing = [f for f in REQUIRED_FIELDS if not row.get(f)]
                if missing:
                    print(f"Warning: skipping row {i} in {transaction_file} "
                          f"(missing field(s): {', '.join(missing)})")
                    continue
                try:
                    row["amount"] = float(row["amount"])
                except (ValueError, TypeError):
                    print(f"Warning: skipping row {i} in {transaction_file} "
                          f"(invalid amount: {row['amount']!r})")
                    continue
                transactions.append(row)
        return transactions
    except FileNotFoundError:
        return []
    except (csv.Error, UnicodeDecodeError, OSError) as e:
        print(f"Warning: {transaction_file} could not be read ({e}). "
              f"Starting with an empty transaction list.")
        return []


def save_transactions(transactions):
    with open(transaction_file, "w", newline="") as file:
        fieldnames = REQUIRED_FIELDS
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)


def load_budget():
    """Load budget.json. Returns {} if missing, invalid JSON, or not
    a JSON object — instead of crashing."""
    try:
        with open(budget_file, "r") as file:
            data = json.load(file)
        if not isinstance(data, dict):
            print(f"Warning: {budget_file} does not contain a valid budget "
                  f"object. Ignoring its contents.")
            return {}
        return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"Warning: {budget_file} is corrupted ({e}). "
              f"Ignoring its contents.")
        return {}
    except OSError as e:
        print(f"Warning: {budget_file} could not be read ({e}).")
        return {}


def save_budget(budget_limit):
    with open(budget_file, "w") as file:
        json.dump(budget_limit, file, indent=2)


def get_budget_limit():
    print("These are the available categories and you have to set limit for each")
    budget_limit = {}
    for cat in BUDGET_CATEGORIES:
        while True:
            raw = input(f"What is your budget for {cat}?: $")
            try:
                budget_limit[cat] = float(raw)
                break
            except ValueError:
                print("  Please enter a number.")
    return budget_limit


# ----------------------------- TRANSACTIONS -----------------------------

def add_transaction(transactions):
    transaction_type = input("Is this an income or expenses?: ").strip().lower()
    category = input("Which category does this belong to?: ").strip().lower()
    while True:
        try:
            amount = float(input("What is the amount?: $"))
            break
        except ValueError:
            print("  Please enter a number.")
    description = input("Give a description in two words or less: ").strip()
    date = datetime.datetime.today().strftime("%Y-%m-%d")
    td = {
        "transaction_type": transaction_type,
        "category": category,
        "amount": amount,
        "description": description,
        "date": date,
    }
    transactions.append(td)
    return transactions


def calculate_balance(transactions):
    total_income = 0
    total_expenses = 0
    for t in transactions:
        if t["transaction_type"] == "income":
            total_income += t["amount"]
        elif t["transaction_type"] == "expenses":
            total_expenses += t["amount"]
    total_balance = total_income - total_expenses
    return total_income, total_expenses, total_balance


def show_balance(transactions):
    total_income, total_expenses, total_balance = calculate_balance(transactions)
    print("_______BALANCE________")
    print(f"Total_income: ${total_income:.2f} ")
    print(f"Total_expenses: ${total_expenses:.2f}")
    print(f"Total_balance: ${total_balance:.2f}")


def show_history(transactions):
    print("---------------VIEW HISTORY---------------")
    if not transactions:
        print("No transactions recorded yet.")
        return
    for t in transactions:
        print("-----------------------------------------")
        print(f"Type: {t['transaction_type'].capitalize()}")
        print(f"Category: {t['category'].capitalize()}")
        print(f"Amount: ${t['amount']:.2f}")
        print(f"Description: {t['description'].capitalize()}")
        print(f"Date: {t['date']}")


def calculate_category_totals(transactions):
    category_totals = {}
    for t in transactions:
        if t["transaction_type"] == "expenses":
            category = t["category"]
            amount = t["amount"]
            category_totals[category] = category_totals.get(category, 0) + amount
    return category_totals


def calculate_savings_rate(transactions):
    total_income, total_expenses, total_balance = calculate_balance(transactions)
    try:
        savings_rate = (total_income - total_expenses) / total_income * 100
    except ZeroDivisionError:
        return "Income can't be zero"
    return float(savings_rate)


def show_breakdown(transactions, budget_limit):
    category_totals = calculate_category_totals(transactions)
    savings_rate = calculate_savings_rate(transactions)
    total_income, total_expenses, total_balance = calculate_balance(transactions)

    print("----------- SPENDING BREAKDOWN -----------")

    if total_expenses == 0:
        print("No expenses recorded.")
    else:
        for category, amount in category_totals.items():
            percentage = (amount / total_expenses) * 100
            print(f"{category.capitalize()}: ${amount:.2f} ({percentage:.1f}%)")
            if category in budget_limit and amount > budget_limit[category]:
                print(f"  Over budget by ${amount - budget_limit[category]:.2f}")

    if isinstance(savings_rate, str):
        print(f"Savings rate: {savings_rate}")
    else:
        print(f"Savings rate: {savings_rate:.2f}%")


# ----------------------------- NEW: DUPLICATES -----------------------------

def check_duplicates(transactions):
    """Detect transactions with identical type, category, amount,
    description, and date. Warns but does not delete anything."""
    seen = {}
    found_any = False
    for t in transactions:
        key = (t["transaction_type"], t["category"], t["amount"],
               t["description"], t["date"])
        if key in seen:
            print(f"Warning: duplicate transaction detected -> "
                  f"{t['transaction_type']} | {t['category']} | "
                  f"${t['amount']:.2f} | {t['description']} | {t['date']}")
            found_any = True
        else:
            seen[key] = True
    if not found_any:
        print("No duplicate transactions found.")


# ----------------------------- NEW: MONTHLY ANALYSIS -----------------------------

def monthly_totals(transactions):
    """Groups expenses by YYYY-MM prefix of date. Returns {month: total}."""
    totals = {}
    for t in transactions:
        if t["transaction_type"] == "expenses":
            month = t["date"][:7]
            totals[month] = totals.get(month, 0) + t["amount"]
    return totals


def compare_months(transactions):
    """Compares the two most recent months THAT HAVE EXPENSE DATA.
    Note: 'most recent' is based on which months appear in your data,
    not strictly consecutive calendar months. If you have expenses in
    Jan and Mar but none in Feb, this compares Jan vs Mar."""
    totals = monthly_totals(transactions)
    months = sorted(totals.keys())

    print("----------- MONTHLY COMPARISON -----------")
    if len(months) < 2:
        print("Not enough monthly data to compare (need expenses in at "
              "least 2 different months).")
        return

    prev_month, current_month = months[-2], months[-1]
    prev_total = totals[prev_month]
    current_total = totals[current_month]

    print(f"{prev_month}: ${prev_total:.2f}")
    print(f"{current_month}: ${current_total:.2f}")

    if prev_total == 0:
        print("Cannot calculate percentage change: previous month had $0 in expenses.")
        return

    change = ((current_total - prev_total) / prev_total) * 100
    if change > 0:
        print(f"Spending is UP by {change:.2f}% compared to {prev_month}.")
    elif change < 0:
        print(f"Spending is DOWN by {abs(change):.2f}% compared to {prev_month}.")
    else:
        print(f"Spending is unchanged compared to {prev_month}.")


def average_daily_spend(transactions):
    """Total expenses divided by number of unique days that have at
    least one expense transaction (not total calendar days)."""
    total_expenses = 0
    unique_days = set()
    for t in transactions:
        if t["transaction_type"] == "expenses":
            total_expenses += t["amount"]
            unique_days.add(t["date"])

    print("----------- AVERAGE DAILY SPEND -----------")
    if not unique_days:
        print("No expense transactions recorded. Cannot calculate average.")
        return

    avg = total_expenses / len(unique_days)
    print(f"Across {len(unique_days)} day(s) with recorded expenses: ${avg:.2f}/day")


# ----------------------------- NEW: EXPORT -----------------------------

def export_report(transactions):
    if not transactions:
        print("No transactions to export.")
        return

    print("Filter by: 1. Category   2. Date range")
    filter_choice = input("Enter your choice (1 or 2): ").strip()

    if filter_choice == "1":
        category = input("Enter category to filter by: ").strip().lower()
        filtered = [t for t in transactions if t["category"].lower() == category]
        filter_desc = f"category_{category.replace(' ', '_')}"
    elif filter_choice == "2":
        start_date = input("Enter start date (YYYY-MM-DD): ").strip()
        end_date = input("Enter end date (YYYY-MM-DD): ").strip()
        try:
            datetime.datetime.strptime(start_date, "%Y-%m-%d")
            datetime.datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Export cancelled.")
            return
        if start_date > end_date:
            print("Start date is after end date. Export cancelled.")
            return
        filtered = [t for t in transactions if start_date <= t["date"] <= end_date]
        filter_desc = f"{start_date}_to_{end_date}"
    else:
        print("Invalid choice. Export cancelled.")
        return

    if not filtered:
        print("No transactions match that filter. Nothing exported.")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"report_{filter_desc}_{timestamp}.txt"

    try:
        with open(filename, "w") as file:
            file.write("=" * 50 + "\n")
            file.write("EXPENSE REPORT\n")
            file.write("=" * 50 + "\n\n")
            total_in = 0
            total_out = 0
            for t in filtered:
                file.write(f"Date:        {t['date']}\n")
                file.write(f"Type:        {t['transaction_type'].capitalize()}\n")
                file.write(f"Category:    {t['category'].capitalize()}\n")
                file.write(f"Amount:      ${t['amount']:.2f}\n")
                file.write(f"Description: {t['description'].capitalize()}\n")
                file.write("-" * 50 + "\n")
                if t["transaction_type"] == "expenses":
                    total_out += t["amount"]
                elif t["transaction_type"] == "income":
                    total_in += t["amount"]
            file.write(f"\nTotal income in report:   ${total_in:.2f}\n")
            file.write(f"Total expenses in report: ${total_out:.2f}\n")
    except OSError as e:
        print(f"Failed to write report: {e}")
        return

    print(f"Report exported successfully to '{filename}' ({len(filtered)} transaction(s)).")


# ----------------------------- NEW: BUDGET MANAGEMENT -----------------------------

def set_budget(budget):
    """Lets the user set/update a limit per category. Saves to
    budget.json after every single change (not just at the end), so
    a crash mid-edit doesn't lose prior edits in this session."""
    print("----------- SET BUDGET LIMITS -----------")
    print("Current budget limits:")
    if budget:
        for cat, limit in budget.items():
            print(f"  {cat.capitalize()}: ${limit:.2f}")
    else:
        print("  No budget set yet.")

    print("\nEnter a new limit for each category, or press Enter to keep the current value.")
    for cat in BUDGET_CATEGORIES:
        current = budget.get(cat)
        current_str = f"${current:.2f}" if current is not None else "not set"
        raw = input(f"{cat.capitalize()} [{current_str}]: $").strip()
        if raw == "":
            continue
        try:
            new_limit = float(raw)
        except ValueError:
            print(f"  Invalid number. Keeping previous value for {cat}.")
            continue
        budget[cat] = new_limit
        save_budget(budget)
        print(f"  Saved: {cat.capitalize()} budget set to ${new_limit:.2f}.")

    return budget


# ----------------------------- MENU / MAIN -----------------------------

def show_menu():
    print("\n========== EXPENSE REPORT SYSTEM ==========")
    print("1. Add transaction")
    print("2. Show balance")
    print("3. Show history")
    print("4. Show breakdown")
    print("5. Monthly comparison")
    print("6. Average daily spend")
    print("7. Export report")
    print("8. Set budget limits")
    print("9. Exit")
    print("============================================")


def main():
    transactions = load_transactions()
    check_duplicates(transactions)

    budget_limit = load_budget()
    if budget_limit == {}:
        budget_limit = get_budget_limit()
        save_budget(budget_limit)

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_transaction(transactions)
            save_transactions(transactions)
        elif choice == "2":
            show_balance(transactions)
        elif choice == "3":
            show_history(transactions)
        elif choice == "4":
            show_breakdown(transactions, budget_limit)
        elif choice == "5":
            compare_months(transactions)
        elif choice == "6":
            average_daily_spend(transactions)
        elif choice == "7":
            export_report(transactions)
        elif choice == "8":
            budget_limit = set_budget(budget_limit)
        elif choice == "9":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()