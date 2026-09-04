expenses = []

print('''==============================
      PERSONAL EXPENSE TRACKER
==============================''')

opr = input('''
1. Add Expense
2. View Expenses
3. Show Total Spending
4. Search Expenses
5. Exit

Enter your choice: ''')


if opr == "1":

    expense_name = input("Enter Your Expense: ")
    amount = int(input("Enter Amount: "))
    category = input("Enter Category: ")

    expense = (expense_name, amount, category)

    expenses.append(expense)

    print("Expense added successfully!")
    print(expenses)


elif opr == "2":

    print(expenses)


elif opr == "3":

    print("Total Spending:", sum(expense[1] for expense in expenses))


elif opr == "4":

    category = input("Enter Category to search: ")

    for expense in expenses:
        if expense[2] == category:
            print(expense)


elif opr == "5":

    print("Thank you for using Personal Expense Tracker!")


else:

    print("Invalid choice!")