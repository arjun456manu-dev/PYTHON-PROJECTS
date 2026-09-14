sales = [1200, 850, 4500, 2300, 780, 5600, 3200]
def calculate_total_sales(sales):
    total_sales = sum(sales)
   
    return total_sales

def calculate_average(sales):
    if len(sales)== 0:
        return 0
    
    return  sum(sales) / len(sales)

def highest_sales(sales):
    highest_sales_amg = max(sales)

    return highest_sales_amg


def high_value_sales(sales, threshold):
    high_value = []

    for sale in sales:
        if sale > threshold:
            high_value.append(sale)

    return high_value

def generate_sales_report(sales):
    print("Total sales:", calculate_total_sales(sales))
    print("Average sales:", calculate_average(sales))
    print("Highest sale:", highest_sales(sales))
    print("High-value sales:", high_value_sales(sales, 3000))

generate_sales_report(sales)