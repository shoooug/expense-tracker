def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Please enter a non-negative number.")
            elif value != value or value in (float("inf"), float("-inf")):
                print("Error: Please enter a valid number.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid number.")


def get_yes_or_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "no"):
            return answer
        print("Error: Please enter 'yes' or 'no'.")


def main():
    print("Welcome to the Monthly Budget Calculator")

    budget = get_positive_number("Enter your monthly budget: ")
    total_expenses = 0

    while True:
        add_expense = get_yes_or_no("Do you want to add an expense? (yes/no): ")

        if add_expense == "yes":
            expense = get_positive_number("Enter expense amount: ")
            total_expenses += expense
        else:
            break

    remaining_balance = budget - total_expenses

    print(f"\nTotal expenses: {total_expenses:.2f}")
    print(f"Remaining balance: {remaining_balance:.2f}")

    if remaining_balance < 0:
        print("Status: Over budget")
    else:
        print("Status: Within budget")


if __name__ == "__main__":
    main()