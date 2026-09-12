transactions = [
    {"id": 101, "amount": 4500, "status": "completed"},
    {"id": 102, "amount": -1200, "status": "completed"},
    {"id": 103, "amount": 3200, "status": "cancelled"},
    {"id": 104, "amount": 7800, "status": "completed"},
    {"id": 105, "amount": 0, "status": "completed"},
    {"id": 106, "amount": 6100, "status": "completed"}
]


def clean_transactions(transactions):
    cleaned_transactions =[]
    for t in transactions:
        if t["status"] =="completed" and t["amount"] > 0:


            cleaned_transactions.append(t)
    total_revenue = 0

    for t in cleaned_transactions:
        if t["amount"] <0:
            cleaned_transactions.append(t)

    for t in cleaned_transactions:
        total_revenue += t["amount"]
        print(total_revenue)

    avg_valid_amt = total_revenue / len(cleaned_transactions)
    print(avg_valid_amt)


    highest = max(cleaned_transactions , key= lambda t: t["amount"])
    print("id",highest["id"])
    print("amount",highest["amount"])

    count = 0 
    for t in cleaned_transactions:
        if t["amount"] > 5000:
            count +=1
    print(count)


        
    return(cleaned_transactions)
cleaned = clean_transactions(transactions)   
print(cleaned)    
















