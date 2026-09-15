sales = [1200, 4500, 2300, 7800, 1500, 6200, 900, 5100]

def analyze_sales(sales):
    high_sales = []
    low_sales =[]
    discounted_sales = []

    for sale in sales:
        if sale >= 5000:
            high_sales.append(sale)
 
        else:
            low_sales.append(sale)


    for sale in high_sales:
     
        discounted_price = sale - (sale * 10 /100)
        discounted_sales.append(discounted_price)
                        

        total_revenue = sum(sales)
    highest = max(high_sales)


    print("High:", high_sales)
    print("Low:", low_sales)
    print("Discounted:", discounted_sales)
    print("Total:", total_revenue)
    print("Highest:", highest)



    return high_sales , low_sales,discounted_sales , total_revenue , highest
     
analyze_sales(sales)