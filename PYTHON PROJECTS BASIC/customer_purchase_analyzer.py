# ================= CUSTOMER PURCHASE ANALYZER ===================

customers = {
    "Rahul": 4500,
    "Priya": 8200,
    "Aman": 2300,
    "Neha": 12500,
    "Rohit": 6700
}

def customer_report(customers):
    total_purchase = sum(customers.values())
    print(total_purchase)

    avg_purchase = sum(customers.values()) / len(customers)
    print(avg_purchase)

    highest_spending = max(customers,key = customers.get)
    print(highest_spending)

    highest_spending_amount = customers[highest_spending]
    print(highest_spending_amount)


    count = 0

    for spent in customers.values():
        if spent > 5000:
            count += 1
    print(count)
    # just a new try  
    print(f"the total number of customer purchse above 50000 are {count}") 

    for customer,spent in customers.items():
        if spent >= 10000:
            print("premium")
        elif 5000 <= spent < 10000:
            print("regular")
        else:
            print("low")

    if total_purchase >= 30000:
        print("target achived")
    else:
        print("not echived")
customer_report(customers)
                         