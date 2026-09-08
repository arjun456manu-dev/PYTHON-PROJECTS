sales = [12000, 15000, 9000, 18000, 22000, 11000, 16000]
total_weekly_sales = sum(sales)
print( total_weekly_sales)
average_daily_sales = (sum(sales)/7)
print(average_daily_sales)
highest_sales_day =  max(sales)
print(highest_sales_day)
lowest_sales_day = min(sales)
print(lowest_sales_day)

count = 0 
for sale in sales :
    if sale > 15000:
        count += 1
print (count)

if total_weekly_sales >= 100000:
    print("target achived")
else:
    print("not achived")

