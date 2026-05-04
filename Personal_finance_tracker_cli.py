def get_budget_limit():
    print("These are the available categories and you have to set limit for each")

    budget_limit = {
        "housing": float(input("What is your budget for housing?: $")),
        "utilities": float(input("What is your budget for utilities?: $")),
        "transportation": float(input("What is your budget for transportation?: $")),
        "food": float(input("What is your budget for food?: $")),
        "health": float(input("What is your budget for health?: $")),
        "personal care": float(input("What is your budget for personal care?: $")),
        "lifestyle": float(input("What is your budget for lifestyle?: $")),
        "leisure": float(input("What is your budget for leisure?: $")),
    }
    return budget_limit

def add_transaction(transactions):

    transaction_type = input("Is this an income or expenses?: ").lower()
    category = input("Which category does this belong to?: ")
    amount = float(input("What is the amount?: $"))
    description = input("Give a description in two words or less: ")
    td = {"transaction_type": transaction_type,
          "category" : category,
          "amount" : amount,
          "description": description
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
    total_balance = total_income - total_expenses
    print("_______BALANCE________")
    print(f"Total_income: ${total_income} ")
    print(f"Total_expenses: ${total_expenses}")
    print(f"Total_balance: ${total_balance}")
def show_history(transactions):
    print("---------------VIEW HISTORY---------------")
    for t in transactions:
        print("-----------------------------------------")
        print(f"Type: {t['transaction_type'].capitalize()}")
        print(f"Category: {t['category'].capitalize()}")
        print(f"Amount: ${t['amount']}")
        print(f"Description: {t['description'].capitalize()}")
def calculate_category_totals(transactions):
    category_totals = {}
    for t in transactions:
        if t["transaction_type"] == "expenses":
            category = t["category"]
            amount = t["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
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

            if category in budget_limit:
                if amount > budget_limit[category]:
                    print(
                        f"  Over budget by ${amount - budget_limit[category]:.2f}"
                    )

    if isinstance(savings_rate, str):
        print(f"Savings rate: {savings_rate}")
    else:
        print(f"Savings rate: {savings_rate:.2f}%")

def show_menu():
    print("1. Add transaction")
    print("2. Show balance")
    print("3. Show history")
    print("4. Show breakdown")
    print("5. Quit")

def main():
    transactions = []
    budget_limit = get_budget_limit()

    while True:
        show_menu()
        choice = input("Enter your choice based on the above options(choose between 1, 2, 3, 4, 5): ")
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            show_balance(transactions)
        elif choice == "3":
            show_history(transactions)
        elif choice == "4":
            show_breakdown(transactions, budget_limit)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()




