transactions = [4500, -1200, 3200, 0, 7800, 6100, -500, 2300]

def clean_transcations(transaction):
    valid_transactions = []
    invalid_transaction = []
    for t in transaction:
        if t > 0:

            valid_transactions.append(t)
           
        else:
            invalid_transaction.append(t)
         

    for s in valid_transactions:
            total_valid_revenue = sum(valid_transactions)
            
    for t in transaction:
         highest = max(transaction)
         


    return  valid_transactions,invalid_transaction,total_valid_revenue , highest

print(clean_transcations(transactions))
