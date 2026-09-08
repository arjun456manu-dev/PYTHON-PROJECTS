# ================ SALES PERFORMANCE ANALYZER====================

sales_data = {
    "Rahul": 45000,
    "Priya": 62000,
    "Aman": 28000,
    "Neha": 75000,
    "Rohit": 55000
}

def sales_report(sales_data):
    total_sales = sum(sales_data.values())
    print(total_sales)

    avergae_sales = sum(sales_data.values()) / len(sales_data)
    print(avergae_sales)

    top_sales_person = max(sales_data , key = sales_data.get)
    print(top_sales_person)
    print(sales_data[top_sales_person])

    count = 0 
    for  sale in sales_data.values():
        if sale > 50000:
            count += 1
    print(count)

    for employee ,sale in sales_data.items():
        if sale >= 60000:
            print("excellent")
        elif  40000 <= sale <= 59000:
            print("good")
        else:
            print("needs imporvement")

        if total_sales >= 250000:
            print("target achived")
        else:
            print("not done")   
sales_report(sales_data) 

