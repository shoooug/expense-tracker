
budget = float(input("Enter your monthly budget: "))
total_expenses = 0

while True:
    add_expense = input("Do you want to add an expense? (yes/no): ").strip().lower()

    if add_expense == "yes":
        expense = float(input("Enter expense amount: "))
        total_expenses += expense
    elif add_expense == "no":
        break
    else:
        print("Please enter yes or no.")

remaining_balance = budget - total_expenses

print(f"Total expenses: {total_expenses:.2f}")
print(f"Remaining balance: {remaining_balance:.2f}")

if remaining_balance < 0:
    print("Over budget")
else:
    print("Within budget")
