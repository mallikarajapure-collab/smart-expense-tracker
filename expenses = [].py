expenses = []
while True:
    print("\n--- SMART EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. Show Total")
    print("3. Show Category Wise")
    print("4. Exit")

    choice = input("Enter choice: ")
        if choice == "1":
        item = input("Enter expense name: ")
        category = input("Enter category (food/travel/shopping): ")
        amount = int(input("Enter amount: "))

        expenses.append((item, category, amount))
        print("Expense added successfully 😊")
        elif choice == "2":
        total = sum(amount for item, category, amount in expenses)
        print("Total Expense:", total)    elif choice == "3":
        print("\n--- CATEGORY WISE EXPENSES ---")
        for item, category, amount in expenses:
            print(category, ":", item, "-", amount)
                elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice 😅")