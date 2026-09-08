inventory = {
    "Laptop": {"stock": 12, "price": 55000},
    "Mouse": {"stock": 45, "price": 800},
    "Keyboard": {"stock": 30, "price": 1500},
    "Monitor": {"stock": 8, "price": 12000},
    "Headphones": {"stock": 20, "price": 2500}
}

def inventory_report(inventory):
    total_product = 0
    for product , details in inventory.items():
        total_product += details["stock"]

   
    total_inventory_value = 0

    for product , details in inventory.items():

        total_inventory_value += details["stock"]*details["price"]
    print(total_inventory_value)

    for product , details in inventory.items():
        product_highest_stock = max(inventory, key=lambda x: inventory[x]["stock"])
        print(product_highest_stock)        

    count = 0

    for product ,details in inventory.items():
        if details["stock"] < 15:
            count += 1
    print(count)

    for product , details in inventory.items():

        if details["stock"] < 10:
            print("low")
        elif 10 <= details["stock"] <= 30 :
            print("normal")
        else:
            print("high")


    if   total_inventory_value >=1000000:
        print("reached target")
    else:
        print("not reached")
inventory_report(inventory)
