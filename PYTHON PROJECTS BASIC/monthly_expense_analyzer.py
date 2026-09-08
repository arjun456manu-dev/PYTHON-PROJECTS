expenses = {
    "rent": 5000,
    "food": 3500,
    "travel": 1200,
    "electricity": 800,
    "entertainment": 1000
}

def expense_report(expenses):
    total_expense = sum(expenses.values())
    print(total_expense)
    average_expense = total_expense / len(expenses)
    print(average_expense)
    highest_expense_category = max(expenses , key = expenses.get)
    print(highest_expense_category)
    highest_expense_amount = expenses[highest_expense_category]
    print(highest_expense_amount)    

    count = 0 
    for expense in expenses.values():
        if expense > 2000:
            count += 1
    print(count)

    if total_expense <= 12000:
        print("budget maintaned")
    elif total_expense == 12000:
        print("budget exceed")
    else:
        print("  ")


expense_report(expenses)