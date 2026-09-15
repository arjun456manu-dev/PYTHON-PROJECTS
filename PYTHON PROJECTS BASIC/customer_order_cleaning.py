orders = [1200, 4500, 1200, -500, 7800, 4500, 0, 3200]

def process_orders(orders):
    posotive_orders = []
    unique_orders=[]
    valid_unique_orders = []

    for o in orders :
        if o >= 0 :
            posotive_orders.append(o)
        else:
            continue

    for o in posotive_orders:
        if o not in unique_orders:
            unique_orders.append(o)

    for o in unique_orders:
        if o >= 0:
            valid_unique_orders.append(o)

    total_valid_revenue = sum(valid_unique_orders)
    highest = max(unique_orders)

    count = len(unique_orders)

    return valid_unique_orders , unique_orders , posotive_orders,highest,valid_unique_orders
valid, invalid, unique, total, highest, count = process_orders(orders)

print("Valid:", valid)
print("Invalid:", invalid)
print("Unique valid orders:", unique)
print("Total revenue:", total)
print("Highest order:", highest)
print("Count:", count)
            
               

